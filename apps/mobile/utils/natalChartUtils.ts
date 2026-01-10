/**
 * Utilitaires pour thème natal et interprétations
 */

import { NatalSubject, ChartPayload } from '../types/natal';
import { tSign, tPlanet } from '../i18n/astro.format';
import CryptoJS from 'crypto-js';

/**
 * Génère un chart_id stable basé sur les données de naissance
 * Hash MD5 de (date, heure, lat, lon, timezone, house_system)
 *
 * IMPORTANT: Le chart_id NE CONTIENT PAS la version du prompt.
 * C'est l'identité stable du thème natal, indépendante des prompts.
 *
 * @param birthDate - Date de naissance (YYYY-MM-DD)
 * @param birthTime - Heure de naissance (HH:MM)
 * @param latitude - Latitude du lieu
 * @param longitude - Longitude du lieu
 * @param timezone - Timezone IANA (ex: "Europe/Paris") ou UTC offset
 * @param houseSystem - Système de maisons (ex: "placidus", "whole_sign")
 * @returns Chart ID stable (hash MD5)
 */
export function getChartId(
  birthDate: string,
  birthTime: string,
  latitude: number,
  longitude: number,
  timezone: string = 'UTC',
  houseSystem: string = 'placidus'
): string {
  // Arrondir lat/lon à 5 décimales pour stabilité
  const lat = latitude.toFixed(5);
  const lon = longitude.toFixed(5);

  // Normaliser house_system (lowercase, trim)
  const hs = houseSystem.toLowerCase().trim();

  // Construire le hash stable
  const data = `${birthDate}|${birthTime}|${lat}|${lon}|${timezone}|${hs}`;
  return CryptoJS.MD5(data).toString();
}

/**
 * Retourne le label court d'une maison astrologique
 *
 * @param house - Numéro de maison (1-12)
 * @returns Label court de la maison
 */
export function getHouseLabel(house: number): string {
  const labels: Record<number, string> = {
    1: "identité, apparence",
    2: "ressources, valeurs",
    3: "communication, environnement proche",
    4: "foyer, racines",
    5: "créativité, plaisir",
    6: "quotidien, service",
    7: "relations, partenariats",
    8: "intimité, transformation",
    9: "philosophie, expansion",
    10: "carrière, accomplissement",
    11: "projets collectifs, idéaux",
    12: "spiritualité, inconscient"
  };

  return labels[house] || "domaine de vie";
}

/**
 * Convertit un nom de planète/point en NatalSubject
 * Gère les variations de nommage (lowercase, underscore, etc.)
 *
 * @param planetName - Nom de la planète (ex: "Sun", "moon", "Mean Node")
 * @returns NatalSubject ou null si non supporté
 */
export function planetNameToSubject(planetName: string): NatalSubject | null {
  const normalized = planetName.toLowerCase().trim().replace(/[\s_-]+/g, '');

  const mapping: Record<string, NatalSubject> = {
    'sun': 'sun',
    'soleil': 'sun',
    'moon': 'moon',
    'lune': 'moon',
    'ascendant': 'ascendant',
    'midheaven': 'midheaven',
    'mc': 'midheaven',
    'milieuduciel': 'midheaven',  // "Milieu du Ciel" normalisé (sans espaces)
    'milieuciel': 'midheaven',
    'mediumcoeli': 'midheaven',  // Format backend normalisé
    'mercury': 'mercury',
    'mercure': 'mercury',
    'venus': 'venus',
    'vénus': 'venus',
    'mars': 'mars',
    'jupiter': 'jupiter',
    'saturn': 'saturn',
    'saturne': 'saturn',
    'uranus': 'uranus',
    'neptune': 'neptune',
    'pluto': 'pluto',
    'pluton': 'pluto',
    'chiron': 'chiron',
    'northnode': 'north_node',
    'noeudnord': 'north_node',
    'nœudnord': 'north_node',
    'meannode': 'north_node',
    'truenode': 'north_node',
    'southnode': 'south_node',
    'noeudssud': 'south_node',
    'nœudsud': 'south_node',
    'lilith': 'lilith',
    'blackmoon': 'lilith',
  };

  return mapping[normalized] || null;
}

/**
 * Construit le payload pour l'API d'interprétation
 *
 * @param subject - Objet céleste
 * @param chartData - Données du thème natal
 * @returns ChartPayload formaté
 */
export function buildSubjectPayload(
  subject: NatalSubject,
  chartData: any
): ChartPayload {
  let sign = '';
  let degree: number | undefined;
  let house: number | undefined;
  let subjectLabel = '';

  // Récupérer les données selon le sujet
  if (subject === 'sun') {
    sign = chartData.sun_sign || '';
    subjectLabel = 'Soleil';
    // Chercher dans planets si disponible - planets est un OBJET, pas un tableau
    // Accès direct par clé au lieu de .find()
    const sunPlanet = chartData.planets?.['sun'] || chartData.planets?.['soleil'];
    if (sunPlanet) {
      degree = sunPlanet.degree;
      house = sunPlanet.house;
    }
  } else if (subject === 'moon') {
    sign = chartData.moon_sign || '';
    subjectLabel = 'Lune';
    // Accès direct par clé au lieu de .find()
    const moonPlanet = chartData.planets?.['moon'] || chartData.planets?.['lune'];
    if (moonPlanet) {
      degree = moonPlanet.degree;
      house = moonPlanet.house;
    }
  } else if (subject === 'ascendant') {
    sign = chartData.ascendant || '';
    subjectLabel = 'Ascendant';
    // L'ascendant est toujours en Maison 1
    house = 1;
  } else if (subject === 'midheaven') {
    subjectLabel = 'Milieu du Ciel';
    // Le Milieu du Ciel est toujours en Maison 10
    house = 10;
    // Chercher dans planets avec différentes clés possibles
    const mcPlanet = chartData.planets?.['Milieu du Ciel'] || 
                     chartData.planets?.['medium_coeli'] || 
                     chartData.planets?.['mc'] ||
                     chartData.planets?.['midheaven'] ||
                     chartData.midheaven;
    
    // #region agent log
    try {
      fetch('http://127.0.0.1:7242/ingest/b9873e08-35c7-4b38-b260-a864e4bb735c', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          location: 'natalChartUtils.ts:160',
          message: 'midheaven payload construction',
          data: {
            mcPlanetFound: !!mcPlanet,
            mcPlanetType: typeof mcPlanet,
            mcPlanetValue: mcPlanet,
            chartDataPlanetsKeys: chartData.planets ? Object.keys(chartData.planets) : [],
            chartDataMidheaven: chartData.midheaven
          },
          timestamp: Date.now(),
          sessionId: 'debug-session',
          runId: 'run1',
          hypothesisId: 'B'
        })
      }).catch(() => {});
    } catch (e) {}
    // #endregion
    
    if (mcPlanet) {
      sign = mcPlanet.sign || (typeof mcPlanet === 'string' ? mcPlanet : '');
      if (typeof mcPlanet === 'object') {
        degree = mcPlanet.degree;
        // house est déjà 10, mais on peut le récupérer si présent
        if (mcPlanet.house) house = mcPlanet.house;
      }
    } else if (chartData.midheaven) {
      // Fallback sur chartData.midheaven si c'est une string
      sign = chartData.midheaven;
    }
    
    // Si toujours pas de signe, essayer de le chercher dans les maisons (MC = cuspide maison 10)
    if (!sign && chartData.houses && chartData.houses['10']) {
      sign = chartData.houses['10'].sign || '';
    }
  } else {
    // Autres planètes - planets est un OBJET avec des clés
    // Chercher la clé correspondant au subject
    let planetData: any = null;
    
    if (chartData.planets && typeof chartData.planets === 'object' && !Array.isArray(chartData.planets)) {
      // Parcourir les clés de l'objet planets
      for (const key of Object.keys(chartData.planets)) {
        const planetSubject = planetNameToSubject(key);
        if (planetSubject === subject) {
          planetData = chartData.planets[key];
          break;
        }
      }
    }

    if (planetData) {
      sign = planetData.sign || '';
      degree = planetData.degree;
      house = planetData.house;
    }

    // Label français
    subjectLabel = tPlanet(subject);
  }

  // Traduire le signe en français
  const signFr = tSign(sign);

  return {
    subject_label: subjectLabel,
    sign: signFr || sign,
    degree,
    house,
    ascendant_sign: chartData.ascendant ? tSign(chartData.ascendant) : undefined,
  };
}

/**
 * Filtre les aspects selon les règles v4 (senior professionnel)
 *
 * Règles v4:
 * - Types majeurs uniquement: conjunction, opposition, square, trine
 * - Orbe strict: <= 6°
 * - Exclure Lilith (mean_lilith, lilith) des aspects affichés
 *
 * @param aspects - Liste brute des aspects
 * @param version - Version d'interprétation (2, 3, ou 4). Défaut: 4 (règles strictes)
 * @returns Aspects filtrés et triés par orbe croissant
 */
export function filterMajorAspectsV4(
  aspects: any[],
  version: number = 4
): any[] {
  // v2/v3: conserver tous les aspects (comportement legacy)
  if (version !== 4) {
    return aspects.slice().sort((a, b) => {
      const orbA = Math.abs(a.orb ?? 999);
      const orbB = Math.abs(b.orb ?? 999);
      return orbA - orbB;
    });
  }

  // v4: filtrage strict
  const MAJOR_ASPECT_TYPES = new Set(['conjunction', 'opposition', 'square', 'trine']);
  const MAX_ORB = 6;

  return aspects
    .filter((aspect) => {
      // 1. Type majeur uniquement
      const type = aspect.type?.toLowerCase();
      if (!type || !MAJOR_ASPECT_TYPES.has(type)) {
        return false;
      }

      // 2. Orbe <= 6°
      const orb = Math.abs(aspect.orb ?? 999);
      if (orb > MAX_ORB) {
        return false;
      }

      // 3. Exclure Lilith (mean_lilith, lilith)
      const planet1 = aspect.planet1?.toLowerCase().replace(/[\s_-]+/g, '') ?? '';
      const planet2 = aspect.planet2?.toLowerCase().replace(/[\s_-]+/g, '') ?? '';

      if (planet1.includes('lilith') || planet2.includes('lilith')) {
        return false;
      }

      return true;
    })
    .sort((a, b) => {
      // Tri par orbe croissant (aspects les plus serrés en premier)
      const orbA = Math.abs(a.orb ?? 999);
      const orbB = Math.abs(b.orb ?? 999);
      return orbA - orbB;
    });
}
