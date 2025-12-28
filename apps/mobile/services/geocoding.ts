/**
 * Service de géocodage via Nominatim OpenStreetMap
 * Convertit un nom de lieu en coordonnées latitude/longitude
 */

export interface GeocodeResult {
  latitude: number;
  longitude: number;
}

/**
 * Géocode un lieu (ville, pays) et retourne les coordonnées
 * @param placeName - Ex: "Paris, France" ou "Livry-Gargan, France"
 * @returns Coordonnées latitude/longitude
 * @throws Error si le lieu est introuvable ou en cas d'erreur réseau
 */
export async function geocodePlace(placeName: string): Promise<GeocodeResult> {
  if (!placeName || placeName.trim().length < 2) {
    throw new Error('Le lieu doit contenir au moins 2 caractères');
  }

  const url = `https://nominatim.openstreetmap.org/search?format=json&limit=1&q=${encodeURIComponent(placeName.trim())}`;
  
  console.log('[Geocoding] Recherche du lieu:', placeName);
  console.log('[Geocoding] URL:', url);
  
  // Créer un AbortController pour gérer le timeout (compatible React Native)
  const controller = new AbortController();
  const timeoutId = setTimeout(() => {
    console.log('[Geocoding] Timeout déclenché');
    controller.abort();
  }, 10000); // 10s timeout
  
  try {
    const response = await fetch(url, {
      headers: {
        'User-Agent': 'AstroiaLunar/1.0 (contact@astroia.app)',
      },
      signal: controller.signal,
    });
    
    clearTimeout(timeoutId);

    console.log('[Geocoding] Réponse status:', response.status);

    if (!response.ok) {
      throw new Error(`Erreur HTTP ${response.status}`);
    }

    const data = await response.json();
    console.log('[Geocoding] Données reçues:', data?.length || 0, 'résultat(s)');
    
    if (!data || data.length === 0) {
      console.log('[Geocoding] Aucun résultat trouvé');
      throw new Error('Lieu introuvable');
    }

    const result = data[0];
    const latitude = parseFloat(result.lat);
    const longitude = parseFloat(result.lon);

    console.log('[Geocoding] Coordonnées trouvées:', { latitude, longitude });

    if (isNaN(latitude) || isNaN(longitude)) {
      throw new Error('Coordonnées invalides retournées par le géocodage');
    }

    return {
      latitude,
      longitude,
    };
  } catch (error: any) {
    clearTimeout(timeoutId);
    console.error('[Geocoding] Erreur:', error.name, error.message);
    if (error.name === 'AbortError' || error.name === 'TimeoutError') {
      throw new Error('Timeout : le géocodage a pris trop de temps');
    }
    if (error.message === 'Lieu introuvable') {
      throw error; // Propager le message exact
    }
    // Si c'est une erreur réseau (pas de réponse), propager le message original
    if (error.message?.includes('Network') || error.message?.includes('Failed to fetch')) {
      throw new Error('Erreur de connexion, vérifiez votre réseau');
    }
    throw new Error('Erreur de connexion, vérifiez votre réseau');
  }
}

