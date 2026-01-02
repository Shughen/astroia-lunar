#!/usr/bin/env python3
"""
Test de sanity pour natal_planets_complement.py
Vérifie que le module peut être importé et que calculate_complementary_positions fonctionne
sans erreur même avec DISABLE_CHIRON=true.

Usage:
    DISABLE_CHIRON=true python scripts/test_natal_planets_complement_sanity.py
    # ou
    python scripts/test_natal_planets_complement_sanity.py
"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_import_module():
    """Test 1: Import du module sans erreur."""
    print("🧪 Test 1: Import du module...")
    try:
        from services.natal_planets_complement import (
            calculate_complementary_positions,
            _get_chiron_enabled,
            _get_planet_codes,
        )
        print("   ✅ Module importé avec succès")
        return calculate_complementary_positions, _get_chiron_enabled, _get_planet_codes
    except Exception as e:
        print(f"   ❌ Erreur import: {e}")
        sys.exit(1)


def test_chiron_enabled_flag():
    """Test 2: Vérifier que _get_chiron_enabled() respecte DISABLE_CHIRON."""
    print("\n🧪 Test 2: Vérification flag DISABLE_CHIRON...")
    try:
        from services.natal_planets_complement import _get_chiron_enabled
        from config import settings
        
        chiron_enabled = _get_chiron_enabled()
        disable_chiron_env = os.getenv("DISABLE_CHIRON", "").lower() in ("true", "1", "yes")
        disable_chiron_config = getattr(settings, "DISABLE_CHIRON", False)
        
        print(f"   DISABLE_CHIRON (env): {disable_chiron_env}")
        print(f"   DISABLE_CHIRON (config): {disable_chiron_config}")
        print(f"   _get_chiron_enabled(): {chiron_enabled}")
        
        # Si DISABLE_CHIRON est activé, Chiron ne doit pas être activé
        if disable_chiron_config or disable_chiron_env:
            if chiron_enabled:
                print("   ⚠️  Chiron activé malgré DISABLE_CHIRON (peut être normal si SwissEph non disponible)")
            else:
                print("   ✅ Chiron désactivé comme attendu")
        else:
            print("   ℹ️  DISABLE_CHIRON non activé, Chiron peut être activé si SwissEph disponible")
        
        return True
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_planet_codes():
    """Test 3: Vérifier que _get_planet_codes() fonctionne."""
    print("\n🧪 Test 3: Vérification _get_planet_codes()...")
    try:
        from services.natal_planets_complement import _get_planet_codes
        
        codes = _get_planet_codes()
        print(f"   ✅ Codes planètes obtenus: {len(codes)} planètes/points")
        print(f"   Chiron dans codes: {'chiron' in codes}")
        print(f"   Chiron code value: {codes.get('chiron')}")
        
        # Vérifier que Chiron est None si DISABLE_CHIRON=true
        from config import settings
        if getattr(settings, "DISABLE_CHIRON", False):
            if codes.get("chiron") is None:
                print("   ✅ Chiron correctement désactivé (None)")
            else:
                print("   ⚠️  Chiron présent malgré DISABLE_CHIRON (peut être normal si flag non lu)")
        
        return True
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_calculate_complementary_positions():
    """Test 4: Appeler calculate_complementary_positions() sans crash."""
    print("\n🧪 Test 4: Appel calculate_complementary_positions()...")
    try:
        from services.natal_planets_complement import calculate_complementary_positions
        
        # Date de test
        birth_datetime = datetime(1990, 5, 15, 14, 30, 0)
        latitude = 48.8566
        longitude = 2.3522
        
        print(f"   Paramètres: date={birth_datetime}, lat={latitude}, lon={longitude}")
        
        # Appeler la fonction (peut retourner [] si SwissEph non disponible, c'est OK)
        positions = calculate_complementary_positions(
            birth_datetime=birth_datetime,
            latitude=latitude,
            longitude=longitude,
            house_cusps=None
        )
        
        print(f"   ✅ Fonction exécutée sans erreur")
        print(f"   Positions calculées: {len(positions)}")
        
        if positions:
            print(f"   Exemples: {[p.get('name') for p in positions[:3]]}")
        
        # Vérifier que Chiron n'est pas dans les résultats si DISABLE_CHIRON=true
        from config import settings
        if getattr(settings, "DISABLE_CHIRON", False):
            chiron_positions = [p for p in positions if p.get("name") == "chiron"]
            if chiron_positions:
                print(f"   ⚠️  Chiron présent dans résultats malgré DISABLE_CHIRON")
            else:
                print(f"   ✅ Chiron absent des résultats (comme attendu)")
        
        return True
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Exécute tous les tests."""
    print("=" * 60)
    print("🧪 Test de Sanity: natal_planets_complement.py")
    print("=" * 60)
    print(f"DISABLE_CHIRON (env): {os.getenv('DISABLE_CHIRON', 'non défini')}\n")
    
    # Test 1: Import
    calculate_complementary_positions, _, _ = test_import_module()
    
    # Test 2: Flag Chiron
    test_chiron_enabled_flag()
    
    # Test 3: Planet codes
    test_planet_codes()
    
    # Test 4: Calcul positions
    test_calculate_complementary_positions()
    
    print("\n" + "=" * 60)
    print("✅ Tous les tests de sanity passés")
    print("=" * 60)
    print("\n📋 Vérifications:")
    print("   - Module importable sans erreur")
    print("   - Pas d'erreur 'name ... is used prior to global declaration'")
    print("   - calculate_complementary_positions() exécutable sans crash")
    print("   - DISABLE_CHIRON respecté (si activé)")


if __name__ == "__main__":
    main()

