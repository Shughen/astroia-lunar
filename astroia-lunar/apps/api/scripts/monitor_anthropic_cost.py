#!/usr/bin/env python3
"""
Script Monitoring Coûts Anthropic - Astroia Lunar
Date: 2026-01-24
Version: 1.0

Usage:
    python scripts/monitor_anthropic_cost.py --daily
    python scripts/monitor_anthropic_cost.py --monthly
    python scripts/monitor_anthropic_cost.py --export costs.json
    python scripts/monitor_anthropic_cost.py --alert  # Avec alertes Slack/Email
"""

import argparse
import sys
import os
import json
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import requests

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings


class AnthropicCostMonitor:
    """Monitor Anthropic API costs and usage"""

    def __init__(self):
        self.api_key = settings.ANTHROPIC_API_KEY
        self.org_id = getattr(settings, 'ANTHROPIC_ORGANIZATION_ID', None)
        self.alert_webhook = getattr(settings, 'COST_ALERT_WEBHOOK', None)
        self.daily_threshold = float(getattr(settings, 'COST_DAILY_THRESHOLD', 5.0))
        self.monthly_threshold = float(getattr(settings, 'COST_MONTHLY_THRESHOLD', 100.0))

    def get_usage_stats(self, start_date: str, end_date: str) -> Dict[str, Any]:
        """
        Récupérer statistiques d'usage Anthropic
        Note: API Anthropic ne fournit pas encore d'endpoint public pour usage stats
        Cette fonction est un placeholder pour future API

        Alternative: Scraper dashboard web ou utiliser métriques Prometheus
        """

        # Pour l'instant, utiliser métriques Prometheus comme source de vérité
        return self._get_prometheus_estimates(start_date, end_date)

    def _get_prometheus_estimates(self, start_date: str, end_date: str) -> Dict[str, Any]:
        """Estimer coûts depuis métriques Prometheus"""

        prometheus_url = getattr(settings, 'PROMETHEUS_URL', 'http://localhost:9090')

        # Query Prometheus pour générations Claude
        query = f'sum(increase(lunar_interpretation_generated_total{{source="claude"}}[{self._get_range_duration(start_date, end_date)}]))'

        try:
            response = requests.get(
                f'{prometheus_url}/api/v1/query',
                params={'query': query},
                timeout=10
            )
            response.raise_for_status()

            data = response.json()
            if data['status'] == 'success' and data['data']['result']:
                generations = int(float(data['data']['result'][0]['value'][1]))

                # Calcul coûts
                # Avec Prompt Caching: $0.002/génération
                # Sans caching: $0.020/génération
                cost_with_caching = generations * 0.002
                cost_without_caching = generations * 0.020
                savings = cost_without_caching - cost_with_caching

                return {
                    'generations': generations,
                    'cost_with_caching': cost_with_caching,
                    'cost_without_caching': cost_without_caching,
                    'savings': savings,
                    'caching_enabled': True,
                    'period': f'{start_date} to {end_date}'
                }

        except Exception as e:
            print(f"⚠️  Erreur récupération métriques Prometheus: {e}")

        return {
            'generations': 0,
            'cost_with_caching': 0.0,
            'cost_without_caching': 0.0,
            'savings': 0.0,
            'caching_enabled': False,
            'period': f'{start_date} to {end_date}',
            'error': 'Prometheus unavailable'
        }

    def _get_range_duration(self, start_date: str, end_date: str) -> str:
        """Convertir date range en duration Prometheus (ex: 24h, 7d)"""
        start = datetime.fromisoformat(start_date)
        end = datetime.fromisoformat(end_date)
        delta = end - start

        if delta.days == 0:
            return f'{delta.seconds // 3600}h'
        elif delta.days < 7:
            return f'{delta.days}d'
        else:
            return f'{delta.days}d'

    def get_daily_report(self) -> Dict[str, Any]:
        """Rapport coûts quotidiens (dernières 24h)"""

        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)

        stats = self.get_usage_stats(
            start_date.isoformat(),
            end_date.isoformat()
        )

        return {
            'report_type': 'daily',
            'date': end_date.strftime('%Y-%m-%d'),
            'period': 'Last 24 hours',
            **stats,
            'threshold': self.daily_threshold,
            'alert': stats['cost_with_caching'] > self.daily_threshold
        }

    def get_monthly_report(self) -> Dict[str, Any]:
        """Rapport coûts mensuels (mois en cours)"""

        end_date = datetime.now()
        start_date = end_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        stats = self.get_usage_stats(
            start_date.isoformat(),
            end_date.isoformat()
        )

        # Projection fin de mois
        days_elapsed = (end_date - start_date).days + 1
        days_in_month = (start_date.replace(month=start_date.month % 12 + 1, day=1) - timedelta(days=1)).day
        projected_cost = (stats['cost_with_caching'] / days_elapsed) * days_in_month

        return {
            'report_type': 'monthly',
            'month': end_date.strftime('%Y-%m'),
            'days_elapsed': days_elapsed,
            'days_total': days_in_month,
            **stats,
            'projected_month_end': projected_cost,
            'threshold': self.monthly_threshold,
            'alert': projected_cost > self.monthly_threshold
        }

    def print_report(self, report: Dict[str, Any]):
        """Afficher rapport formaté dans console"""

        print(f"\n{'='*70}")
        if report['report_type'] == 'daily':
            print(f"📊 Rapport Coûts Quotidiens - {report['date']}")
        else:
            print(f"📊 Rapport Coûts Mensuels - {report['month']}")
        print(f"{'='*70}\n")

        print(f"Période : {report['period']}")
        print(f"Générations Claude : {report['generations']:,}")
        print()

        print("💰 Coûts :")
        print(f"  Avec Prompt Caching    : ${report['cost_with_caching']:.3f}")
        print(f"  Sans caching (théorique): ${report['cost_without_caching']:.3f}")
        print(f"  Économie caching       : ${report['savings']:.3f} ({report['savings']/report['cost_without_caching']*100:.0f}%)" if report['cost_without_caching'] > 0 else "")
        print()

        if report['report_type'] == 'monthly':
            print(f"📈 Projection :")
            print(f"  Jours écoulés  : {report['days_elapsed']}/{report['days_total']}")
            print(f"  Coût projeté fin mois : ${report['projected_month_end']:.2f}")
            print()

        print(f"⚠️  Seuil configuré : ${report['threshold']:.2f}")

        if report['alert']:
            print(f"\n🚨 ALERTE : Seuil dépassé ! (${report.get('cost_with_caching', 0):.2f} > ${report['threshold']:.2f})")
        else:
            print(f"\n✅ OK : En dessous du seuil (${report.get('cost_with_caching', 0):.2f} < ${report['threshold']:.2f})")

        print(f"\n{'='*70}\n")

    def send_alert(self, report: Dict[str, Any]):
        """Envoyer alerte si seuil dépassé"""

        if not report['alert']:
            return

        if not self.alert_webhook:
            print("⚠️  Aucun webhook configuré pour alertes (COST_ALERT_WEBHOOK)")
            return

        # Format message Slack
        if report['report_type'] == 'daily':
            title = f"🚨 Alerte Coûts Quotidiens - {report['date']}"
            cost = report['cost_with_caching']
        else:
            title = f"🚨 Alerte Coûts Mensuels - {report['month']}"
            cost = report.get('projected_month_end', report['cost_with_caching'])

        message = {
            "text": title,
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": title
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Générations:*\n{report['generations']:,}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Coût:*\n${cost:.2f}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Seuil:*\n${report['threshold']:.2f}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Dépassement:*\n{((cost - report['threshold']) / report['threshold'] * 100):.0f}%"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "📊 *Actions recommandées:*\n• Vérifier cache hit rate\n• Vérifier force_regenerate usage\n• Considérer switch Opus → Sonnet"
                    }
                }
            ]
        }

        try:
            response = requests.post(
                self.alert_webhook,
                json=message,
                timeout=10
            )
            response.raise_for_status()
            print("✅ Alerte envoyée avec succès")

        except Exception as e:
            print(f"❌ Erreur envoi alerte : {e}")

    def export_report(self, report: Dict[str, Any], output_file: str):
        """Exporter rapport en JSON"""

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)

        print(f"✅ Rapport exporté : {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Monitorer coûts Anthropic API"
    )
    parser.add_argument(
        "--daily",
        action="store_true",
        help="Rapport coûts quotidiens (dernières 24h)"
    )
    parser.add_argument(
        "--monthly",
        action="store_true",
        help="Rapport coûts mensuels (mois en cours)"
    )
    parser.add_argument(
        "--alert",
        action="store_true",
        help="Envoyer alerte si seuil dépassé"
    )
    parser.add_argument(
        "--export",
        type=str,
        help="Exporter rapport vers fichier JSON"
    )

    args = parser.parse_args()

    monitor = AnthropicCostMonitor()

    # Générer rapport
    if args.monthly:
        report = monitor.get_monthly_report()
    else:
        # Daily par défaut
        report = monitor.get_daily_report()

    # Afficher rapport
    monitor.print_report(report)

    # Alertes si demandé
    if args.alert:
        monitor.send_alert(report)

    # Export si demandé
    if args.export:
        monitor.export_report(report, args.export)


if __name__ == "__main__":
    main()
