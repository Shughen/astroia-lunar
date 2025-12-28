"""
Helpers pour valider les clés API (détection des placeholders)
"""

from typing import Optional


# Liste des valeurs considérées comme "non configurées" (placeholders)
_PLACEHOLDER_VALUES = {
    "__TO_FILL_LATER__",
    "TO_FILL_LATER",
    "__TO_FILL_LATER",
    "changeme",
    "xxx",
    "your_key_here",
    "placeholder",
    "secret",
    "token",
}


def is_configured_api_key(value: Optional[str]) -> bool:
    """
    Vérifie si une clé API est configurée (non placeholder)
    
    Considère comme NON configuré :
    - None
    - "" (chaîne vide)
    - Placeholders courants (__TO_FILL_LATER__, changeme, xxx, etc.)
    
    Args:
        value: La valeur de la clé API à vérifier
        
    Returns:
        True si la clé est configurée (non placeholder)
        False si la clé est vide ou placeholder
    """
    if not value:
        return False
    
    # Normaliser : strip + lowercase pour comparaison
    normalized = value.strip().lower()
    
    # Vérifier si c'est un placeholder connu
    if normalized in _PLACEHOLDER_VALUES:
        return False
    
    # Vérifier si c'est très court (probablement un placeholder)
    if len(normalized) < 10:
        return False
    
    # Si on arrive ici, c'est probablement une vraie clé
    return True

