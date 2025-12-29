"""
Utilitaires pour la détection automatique de timezone depuis les coordonnées GPS
Basé sur la logique de l'ancienne app
"""


def guess_timezone_from_coords(latitude: float, longitude: float) -> str:
    """
    Devine le timezone depuis les coordonnées GPS (mapping simplifié)
    
    Args:
        latitude: Latitude en degrés décimaux
        longitude: Longitude en degrés décimaux
    
    Returns:
        Timezone IANA (ex: 'America/Manaus', 'Europe/Paris')
    """
    # Europe (lon: -10 à 40)
    if -10 <= longitude <= 10:
        return 'Europe/Paris'  # UTC+1
    if 10 < longitude <= 30:
        return 'Europe/Berlin'  # UTC+1/2
    if 30 < longitude <= 45:
        return 'Europe/Moscow'  # UTC+3
    
    # Amériques
    if -130 <= longitude <= -120:
        return 'America/Los_Angeles'  # UTC-8
    if -120 < longitude <= -105:
        return 'America/Denver'  # UTC-7
    if -105 < longitude <= -90:
        return 'America/Chicago'  # UTC-6
    # Amérique du Sud (vérifier AVANT New_York car il y a chevauchement)
    if -75 <= longitude <= -34:
        if latitude < -15:
            return 'America/Sao_Paulo'  # Brésil Sud
        return 'America/Manaus'  # Brésil Nord/Amazonie
    if -90 < longitude <= -60:
        return 'America/New_York'  # UTC-5
    
    # Asie
    if 100 <= longitude <= 110:
        return 'Asia/Bangkok'  # UTC+7
    if 110 < longitude <= 125:
        return 'Asia/Shanghai'  # UTC+8
    if 125 < longitude <= 145:
        return 'Asia/Tokyo'  # UTC+9
    if 145 < longitude <= 180:
        return 'Pacific/Auckland'  # UTC+12
    
    # Afrique
    if -5 <= longitude <= 15 and -35 <= latitude <= 37:
        return 'Africa/Cairo'
    
    # Défaut
    return 'UTC'


def get_timezone_for_birth_place(
    latitude: float,
    longitude: float,
    provided_timezone: str = "Europe/Paris"
) -> str:
    """
    Détermine la timezone à utiliser pour un lieu de naissance.
    Si la timezone fournie est la valeur par défaut "Europe/Paris", 
    on détecte automatiquement depuis les coordonnées.
    
    Args:
        latitude: Latitude en degrés décimaux
        longitude: Longitude en degrés décimaux
        provided_timezone: Timezone fournie par l'utilisateur (défaut: "Europe/Paris")
    
    Returns:
        Timezone IANA à utiliser
    """
    # Si la timezone fournie est la valeur par défaut, on détecte automatiquement
    if provided_timezone == "Europe/Paris":
        detected_timezone = guess_timezone_from_coords(latitude, longitude)
        return detected_timezone
    
    # Sinon, on utilise la timezone fournie
    return provided_timezone

