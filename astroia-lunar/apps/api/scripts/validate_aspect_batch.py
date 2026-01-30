#!/usr/bin/env python3
"""
Script de validation des interprétations d'aspects générées

Usage:
    python validate_aspect_batch.py --input data/batches/batch_01.json --strict

V

alide:
- Format markdown
- Longueurs des sections
- Absence de jargon technique
- Présence de toutes les sections requises
"""

import json
import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple

# === CRITÈRES DE VALIDATION ===

JARGON_BLACKLIST = [
    'symbiose',
    'indissociation',
    'contextualiser',
    'observer',
    'fusion fonctionnelle',
    'considérer',
    'dissocier',
]

LENGTH_CONSTRAINTS = {
    'summary': (50, 80),
    'manifestation': (350, 650),
    'advice': (100, 200),
    'shadow': (80, 150),
}


# === FONCTIONS ===

def check_jargon(text: str) -> List[str]:
    """Vérifie la présence de jargon technique."""
    found = []
    text_lower = text.lower()
    for word in JARGON_BLACKLIST:
        if word in text_lower:
            found.append(word)
    return found


def validate_aspect(aspect: Dict, strict: bool = False) -> Tuple[bool, List[str]]:
    """
    Valide un aspect généré.

    Returns:
        (is_valid, warnings)
    """
    warnings = []
    is_valid = True

    planet1 = aspect.get('planet1', '?')
    planet2 = aspect.get('planet2', '?')
    aspect_type = aspect.get('aspect_type', '?')
    aspect_id = f"{planet1}_{aspect_type}_{planet2}"

    # Vérifier version sélectionnée (ou A par défaut)
    selected = aspect.get('selected', 'a')
    version_key = f"version_{selected}"

    if version_key not in aspect:
        warnings.append(f"{aspect_id}: Version {selected} introuvable")
        return False, warnings

    version_data = aspect[version_key]
    parsed = version_data.get('parsed', {})
    markdown = version_data.get('markdown', '')

    # 1. Vérifier présence sections requises
    if not parsed.get('summary'):
        warnings.append(f"{aspect_id}: Section 'summary' manquante")
        is_valid = False

    if not parsed.get('manifestation'):
        warnings.append(f"{aspect_id}: Section 'manifestation' manquante")
        is_valid = False

    if not parsed.get('advice'):
        warnings.append(f"{aspect_id}: Section 'advice' manquante")
        is_valid = False

    if not parsed.get('shadow'):
        warnings.append(f"{aspect_id}: Section 'shadow' (Attention) manquante")
        is_valid = False

    # 2. Vérifier longueurs
    for section, (min_len, max_len) in LENGTH_CONSTRAINTS.items():
        text = parsed.get(section, '')
        if text:
            length = len(text)
            if length < min_len:
                msg = f"{aspect_id}: {section} trop court ({length} < {min_len})"
                if strict:
                    is_valid = False
                warnings.append(msg)
            elif length > max_len:
                msg = f"{aspect_id}: {section} trop long ({length} > {max_len})"
                if strict:
                    is_valid = False
                warnings.append(msg)

    # 3. Vérifier absence de jargon
    jargon_found = check_jargon(markdown)
    if jargon_found:
        msg = f"{aspect_id}: Jargon détecté: {', '.join(jargon_found)}"
        warnings.append(msg)
        if strict:
            is_valid = False

    # 4. Vérifier format markdown (présence des sections ##)
    required_sections = [
        "L'énergie de cet aspect",
        "Manifestations concrètes",
        "Conseil pratique",
        "Attention"
    ]

    for section in required_sections:
        if f"## {section}" not in markdown and f"## {section.replace('é', 'e')}" not in markdown:
            warnings.append(f"{aspect_id}: Section markdown '## {section}' manquante")
            is_valid = False

    return is_valid, warnings


def validate_batch(batch_file: str, strict: bool = False, output_file: str = None):
    """Valide un batch complet."""

    with open(batch_file, 'r', encoding='utf-8') as f:
        batch_data = json.load(f)

    batch_number = batch_data.get('batch_number', '?')
    aspects = batch_data.get('aspects', [])

    print(f"=== Validation Batch {batch_number} ===\n")

    total = len(aspects)
    valid_count = 0
    warning_count = 0
    all_warnings = []

    for aspect in aspects:
        is_valid, warnings = validate_aspect(aspect, strict=strict)

        if is_valid:
            valid_count += 1
        if warnings:
            warning_count += len(warnings)
            all_warnings.extend(warnings)

    print(f"✅ {valid_count}/{total} aspects validés")
    print(f"⚠️  {warning_count} warning(s)")

    if all_warnings:
        print("\nDétails :\n")
        for warning in all_warnings:
            print(f"  - {warning}")

    # Afficher coût et durée
    cost = batch_data.get('cost_usd', 0)
    print(f"\n💰 Coût total : ${cost:.2f} USD")

    # Sauvegarder rapport si demandé
    if output_file:
        report = {
            "batch_number": batch_number,
            "total_aspects": total,
            "valid_aspects": valid_count,
            "warning_count": warning_count,
            "warnings": all_warnings,
            "cost_usd": cost
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"\n📄 Rapport sauvegardé : {output_file}")

    # Code de sortie
    if strict and valid_count < total:
        print("\n❌ Validation échouée (mode strict)")
        return 1
    else:
        print("\n✅ Validation terminée")
        return 0


def main():
    parser = argparse.ArgumentParser(description="Valider un batch d'interprétations")
    parser.add_argument('--input', required=True, help="Fichier batch JSON à valider")
    parser.add_argument('--strict', action='store_true', help="Mode strict (échec si warnings)")
    parser.add_argument('--output', help="Fichier de sortie pour le rapport (optionnel)")

    args = parser.parse_args()

    exit_code = validate_batch(args.input, strict=args.strict, output_file=args.output)
    return exit_code


if __name__ == '__main__':
    exit(main())
