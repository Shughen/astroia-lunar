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
    'mileuduciel': 'midheaven',
    'milieuciel': 'midheaven',
    'mediumcoeli': 'midheaven',
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
    sign = chartData.midheaven || '';
    subjectLabel = 'Milieu du Ciel';
    // Le Milieu du Ciel est toujours en Maison 10
    house = 10;
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
