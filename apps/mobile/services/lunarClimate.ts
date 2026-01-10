/**
 * Service de calcul du Climat Lunaire quotidien
 * Logique simple sans IA : position Lune + maisons + aspects
 */

import { CLIMATE_MESSAGES, FALLBACK_MESSAGES, ClimateTone, ClimateMessage } from '../constants/climateMessages';

export interface MoonPosition {
  sign: string;
  degree: number; // 0-360
  phase: string; // Ex: "Nouvelle Lune", "Pleine Lune"
}

// Utiliser les types existants du store pour compatibilité
interface House {
  number: number;
  sign: string;
  degree: number; // Degree de la cuspide
}

interface Planet {
  name: string;
  sign: string;
  degree: number;
  house: number;
  retrograde?: boolean;
}

export interface NatalChart {
  houses?: House[] | Record<string, any>; // Peut être array ou objet (dictionnaire)
  planets?: Planet[] | Record<string, any>; // Peut être array ou objet (dictionnaire)
  sun_sign?: string;
  moon_sign?: string;
  ascendant?: string;
}

export interface DailyLunarClimate {
  theme: string;
  message: string;
  phase: string;
  tone: ClimateTone;
  hasFullChart: boolean; // Indique si basé sur chart complet ou fallback
}

/**
 * Trouve la maison activée par la Lune transit
 * Gère les cas où houses est un array ou un objet (dictionnaire)
 */
function findActivatedHouse(houses: House[] | Record<string, any> | undefined, moonDegree: number): number {
  // Les maisons sont définies par leurs cuspides (degrés de début)
  // On cherche dans quelle tranche tombe moonDegree

  if (!houses) {
    return 1; // Fallback si pas de maisons
  }

  // Convertir houses en array si c'est un objet
  let housesArray: House[];
  if (Array.isArray(houses)) {
    housesArray = houses;
  } else if (typeof houses === 'object' && houses !== null) {
    // Convertir l'objet en array : Object.entries puis mapper
    // Format API: {"1": {sign: "...", degree: ...}, "2": {...}, ...}
    housesArray = Object.entries(houses)
      .map(([key, value]: [string, any]) => {
        // Parser le numéro de maison depuis la clé (string "1", "2", etc.)
        const houseNum = parseInt(key);
        
        // Si value est un objet avec sign/degree (format API)
        if (value && typeof value === 'object') {
          return {
            number: !isNaN(houseNum) && houseNum > 0 && houseNum <= 12 ? houseNum : 1,
            sign: value.sign || '',
            degree: typeof value.degree === 'number' ? value.degree : (typeof value.degree === 'string' ? parseFloat(value.degree) : 0),
          };
        }
        
        // Fallback si value n'est pas un objet
        return {
          number: !isNaN(houseNum) && houseNum > 0 && houseNum <= 12 ? houseNum : 1,
          sign: '',
          degree: 0,
        };
      })
      .filter((h): h is House => h.number > 0 && h.number <= 12)
      .sort((a, b) => a.number - b.number); // Trier par numéro de maison
  } else {
    return 1; // Fallback si format inattendu
  }

  if (housesArray.length === 0) {
    return 1; // Fallback si pas de maisons valides
  }

  // Vérifier que housesArray est bien un array avant d'utiliser le spread operator
  if (!Array.isArray(housesArray)) {
    console.error('[lunarClimate] housesArray is not an array!', {
      type: typeof housesArray,
      value: housesArray,
    });
    return 1; // Fallback
  }

  // Trier les maisons par degree
  try {
    // Utiliser Array.from() au lieu de spread operator pour plus de sécurité
    const sortedHouses = Array.from(housesArray).sort((a, b) => a.degree - b.degree);

    for (let i = 0; i < sortedHouses.length; i++) {
      const currentHouse = sortedHouses[i];
      const nextHouse = sortedHouses[(i + 1) % sortedHouses.length];

      const startDegree = currentHouse.degree;
      const endDegree = nextHouse.degree;

      // Gérer le cas où la maison traverse le 0° (ex: M12 à 350° → M1 à 10°)
      if (endDegree < startDegree) {
        // Maison traverse 360° → 0°
        if (moonDegree >= startDegree || moonDegree < endDegree) {
          return currentHouse.number;
        }
      } else {
        // Maison normale
        if (moonDegree >= startDegree && moonDegree < endDegree) {
          return currentHouse.number;
        }
      }
    }

    // Fallback : retourner maison 1
    return 1;
  } catch (error: any) {
    console.error('[lunarClimate] Erreur dans findActivatedHouse:', error);
    return 1; // Fallback en cas d'erreur
  }
}

/**
 * Trouve les aspects majeurs entre Lune transit et planètes natales
 * Retourne le tone (harmonieux/tendu/neutre)
 * Gère les cas où planets est un array ou un objet (dictionnaire)
 */
function findMajorAspects(
  moonDegree: number,
  natalPlanets: Planet[] | Record<string, any> | undefined
): ClimateTone {
  if (!natalPlanets) {
    return 'neutre';
  }

  // Convertir planets en array si c'est un objet
  let planetsArray: Planet[];
  if (Array.isArray(natalPlanets)) {
    planetsArray = natalPlanets;
  } else if (typeof natalPlanets === 'object' && natalPlanets !== null) {
    // Convertir l'objet en array : Object.entries puis mapper
    // Format API: {"Sun": {sign: "...", degree: ..., house: ...}, "Moon": {...}, ...}
    planetsArray = Object.entries(natalPlanets)
      .map(([name, value]: [string, any]) => {
        // Si value est un objet avec sign/degree/house (format API)
        if (value && typeof value === 'object') {
          return {
            name: name,
            sign: value.sign || '',
            degree: typeof value.degree === 'number' ? value.degree : (typeof value.degree === 'string' ? parseFloat(value.degree) : 0),
            house: typeof value.house === 'number' ? value.house : (typeof value.house === 'string' ? parseInt(value.house) : 0),
            retrograde: value.retrograde || false,
          };
        }
        
        // Fallback si value n'est pas un objet
        return {
          name: name,
          sign: '',
          degree: 0,
          house: 0,
          retrograde: false,
        };
      })
      .filter((p): p is { name: string; sign: any; degree: any; house: any; retrograde: any } => p.name !== undefined && p.name !== null);
  } else {
    return 'neutre';
  }

  if (planetsArray.length === 0) {
    return 'neutre';
  }

  // Vérifier que planetsArray est bien un array avant d'itérer
  if (!Array.isArray(planetsArray)) {
    console.error('[lunarClimate] planetsArray is not an array!', {
      type: typeof planetsArray,
      value: planetsArray,
    });
    return 'neutre';
  }

  let closestAspect: { type: string; orb: number } | null = null;

  // Aspects majeurs : conjonction (0°), sextile (60°), carré (90°), trigone (120°), opposition (180°)
  const aspectAngles = {
    conjunction: { angle: 0, orb: 8, tone: 'harmonieux' as ClimateTone },
    sextile: { angle: 60, orb: 6, tone: 'harmonieux' as ClimateTone },
    square: { angle: 90, orb: 8, tone: 'tendu' as ClimateTone },
    trine: { angle: 120, orb: 8, tone: 'harmonieux' as ClimateTone },
    opposition: { angle: 180, orb: 8, tone: 'tendu' as ClimateTone },
  };

  // Parcourir toutes les planètes natales
  try {
    for (const planet of planetsArray) {
      const planetDegree = planet.degree;

      // Calculer la distance angulaire
      let distance = Math.abs(moonDegree - planetDegree);
      if (distance > 180) distance = 360 - distance; // Prendre le plus court chemin

      // Vérifier chaque type d'aspect
      for (const [aspectType, aspectConfig] of Object.entries(aspectAngles)) {
        const orb = Math.abs(distance - aspectConfig.angle);

        if (orb <= aspectConfig.orb) {
          // Aspect trouvé
          if (!closestAspect || orb < closestAspect.orb) {
            closestAspect = {
              type: aspectType,
              orb,
            };

            // Si aspect très exact (orb < 2°), on privilégie son tone
            if (orb < 2) {
              return aspectConfig.tone;
            }
          }
        }
      }
    }

    // Si aucun aspect exact, retourner le tone du plus proche trouvé
    if (closestAspect) {
      const aspectConfig = Object.values(aspectAngles).find(
        a => a.angle === (closestAspect!.type === 'conjunction' ? 0 :
                         closestAspect!.type === 'sextile' ? 60 :
                         closestAspect!.type === 'square' ? 90 :
                         closestAspect!.type === 'trine' ? 120 : 180)
      );
      return aspectConfig?.tone || 'neutre';
    }

    // Pas d'aspect majeur trouvé
    return 'neutre';
  } catch (error: any) {
    console.error('[lunarClimate] Erreur dans findMajorAspects:', error);
    return 'neutre'; // Fallback en cas d'erreur
  }
}

/**
 * Calcule le Climat Lunaire quotidien
 */
export function calculateDailyLunarClimate(
  moonPosition: MoonPosition,
  natalChart?: NatalChart | null
): DailyLunarClimate {
  // Vérifier si houses existe et n'est pas vide (gère array et objet)
  const hasHouses = natalChart?.houses && (
    Array.isArray(natalChart.houses) 
      ? natalChart.houses.length > 0 
      : Object.keys(natalChart.houses).length > 0
  );
  
  if (!natalChart || !hasHouses) {
    const fallbackMessage = FALLBACK_MESSAGES.phase[moonPosition.phase] || {
      theme: 'Observation',
      message: 'La Lune poursuit son cycle. Moment pour observer tes ressentis intérieurs.',
    };

    return {
      ...fallbackMessage,
      phase: moonPosition.phase,
      tone: 'neutre',
      hasFullChart: false,
    };
  }

  // 1. Identifier la maison activée
  const activatedHouse = findActivatedHouse(natalChart.houses, moonPosition.degree);

  // 2. Déterminer le tone selon les aspects
  const tone = natalChart.planets
    ? findMajorAspects(moonPosition.degree, natalChart.planets)
    : 'neutre';

  // 3. Récupérer le message correspondant
  const messageData = CLIMATE_MESSAGES[activatedHouse]?.[tone] || CLIMATE_MESSAGES[1].neutre;

  return {
    ...messageData,
    phase: moonPosition.phase,
    tone,
    hasFullChart: true,
  };
}
