"""
Services de génération de rapports (P5)
Génère des rapports mensuels en HTML/PDF combinant LR report, transits et événements
"""

from typing import Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


# Template HTML simple pour le rapport mensuel
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport Lunaire - {month}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a0b2e 0%, #2d1b4e 100%);
            color: #ffffff;
            padding: 40px;
            margin: 0;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(42, 26, 78, 0.9);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 10px 50px rgba(0, 0, 0, 0.5);
        }}
        h1 {{
            color: #ffd700;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        h2 {{
            color: #b794f6;
            border-bottom: 2px solid #b794f6;
            padding-bottom: 10px;
            margin-top: 30px;
        }}
        h3 {{
            color: #ffd700;
            margin-top: 20px;
        }}
        .section {{
            margin-bottom: 30px;
        }}
        .insight {{
            background: rgba(183, 148, 246, 0.2);
            padding: 15px;
            border-left: 4px solid #b794f6;
            margin: 10px 0;
            border-radius: 5px;
        }}
        .aspect {{
            background: rgba(255, 215, 0, 0.1);
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            color: #a0a0b0;
            font-size: 0.9em;
        }}
        ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        li {{
            padding: 5px 0;
        }}
        li:before {{
            content: "🌙 ";
            margin-right: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🌙 Rapport Lunaire</h1>
        <p style="text-align: center; color: #b794f6; font-size: 1.2em;">{month}</p>
        
        <div class="section">
            <h2>📊 Révolution Lunaire</h2>
            {lunar_return_section}
        </div>
        
        <div class="section">
            <h2>🔄 Transits du Mois</h2>
            {transits_section}
        </div>
        
        <div class="section">
            <h2>📅 Événements Lunaires</h2>
            {events_section}
        </div>
        
        <div class="footer">
            <p>Généré le {generated_at} par Astroia Lunar</p>
            <p>🌙 ⭐ ✨</p>
        </div>
    </div>
</body>
</html>
"""


def generate_lunar_return_section(lr_data: Optional[Dict[str, Any]]) -> str:
    """Génère la section révolution lunaire du rapport"""
    if not lr_data:
        return "<p>Aucune données de révolution lunaire disponibles.</p>"
    
    html = "<div class='insight'>"
    
    if "moon" in lr_data:
        moon = lr_data["moon"]
        html += f"<p><strong>Lune en {moon.get('sign', 'N/A')}</strong> - Maison {moon.get('house', 'N/A')}</p>"
    
    if "interpretation" in lr_data:
        interp = lr_data["interpretation"]
        if isinstance(interp, dict):
            html += f"<p>{interp.get('summary', '')}</p>"
            if "themes" in interp:
                html += "<ul>"
                for theme in interp["themes"][:5]:
                    html += f"<li>{theme}</li>"
                html += "</ul>"
        elif isinstance(interp, str):
            html += f"<p>{interp}</p>"
    
    html += "</div>"
    return html


def generate_transits_section(transits_data: Optional[Dict[str, Any]]) -> str:
    """Génère la section transits du rapport"""
    if not transits_data or "insights" not in transits_data:
        return "<p>Aucun transit significatif ce mois-ci.</p>"
    
    insights = transits_data["insights"]
    html = ""
    
    if "insights" in insights and insights["insights"]:
        html += "<div class='insight'><h3>Points Clés</h3><ul>"
        for insight in insights["insights"][:5]:
            html += f"<li>{insight}</li>"
        html += "</ul></div>"
    
    if "major_aspects" in insights and insights["major_aspects"]:
        html += "<h3>Aspects Majeurs</h3>"
        for aspect in insights["major_aspects"][:5]:
            html += f"""
            <div class='aspect'>
                <strong>{aspect.get('transit_planet', '')} {aspect.get('aspect', '')} {aspect.get('natal_planet', '')}</strong>
                <br>Orbe: {aspect.get('orb', 0):.1f}°
                {f"<br>{aspect.get('interpretation', '')}" if aspect.get('interpretation') else ''}
            </div>
            """
    
    return html


def generate_events_section(events_data: Optional[list]) -> str:
    """Génère la section événements lunaires du rapport"""
    if not events_data:
        return "<p>Aucun événement lunaire spécial ce mois-ci.</p>"
    
    html = "<ul>"
    for event in events_data[:10]:
        date = event.get("date", "N/A")
        title = event.get("title", "Événement")
        html += f"<li><strong>{date}</strong> - {title}</li>"
    html += "</ul>"
    
    return html


async def generate_monthly_report(
    user_id: int,
    month: str,
    lunar_return_data: Optional[Dict[str, Any]] = None,
    transits_data: Optional[Dict[str, Any]] = None,
    events_data: Optional[list] = None
) -> Dict[str, str]:
    """
    Génère un rapport mensuel HTML combinant LR report, transits et événements.
    
    Args:
        user_id: ID de l'utilisateur
        month: Mois au format YYYY-MM
        lunar_return_data: Données du rapport lunaire
        transits_data: Données des transits
        events_data: Liste des événements lunaires
        
    Returns:
        {
            "html": "<html>...</html>",
            "pdf_url": "optionnel, si génération PDF activée"
        }
    """
    logger.info(f"📝 Génération rapport mensuel pour user {user_id}, mois {month}")
    
    try:
        # Générer les sections
        lr_section = generate_lunar_return_section(lunar_return_data)
        transits_section = generate_transits_section(transits_data)
        events_section = generate_events_section(events_data)
        
        # Remplir le template
        html_content = HTML_TEMPLATE.format(
            month=month,
            lunar_return_section=lr_section,
            transits_section=transits_section,
            events_section=events_section,
            generated_at=datetime.now().strftime("%d/%m/%Y à %H:%M")
        )
        
        # TODO: Génération PDF avec WeasyPrint si activé
        # from weasyprint import HTML
        # pdf_bytes = HTML(string=html_content).write_pdf()
        
        logger.info(f"✅ Rapport mensuel généré ({len(html_content)} caractères)")
        
        return {
            "html": html_content,
            # "pdf_url": f"/reports/{user_id}/{month}.pdf"  # À implémenter
        }
        
    except Exception as e:
        logger.error(f"❌ Erreur génération rapport: {str(e)}")
        raise

