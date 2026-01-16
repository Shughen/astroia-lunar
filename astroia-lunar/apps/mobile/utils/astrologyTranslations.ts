/**
 * Traductions astrologie EN → FR
 */

// Planètes
const PLANETS: Record<string, string> = {
  'Sun': 'Soleil',
  'Moon': 'Lune',
  'Mercury': 'Mercure',
  'Venus': 'Vénus',
  'Mars': 'Mars',
  'Jupiter': 'Jupiter',
  'Saturn': 'Saturne',
  'Uranus': 'Uranus',
  'Neptune': 'Neptune',
  'Pluto': 'Pluton',
  'North Node': 'Nœud Nord',
  'South Node': 'Nœud Sud',
  'Chiron': 'Chiron',
  'Ascendant': 'Ascendant',
  'Midheaven': 'Milieu du Ciel',
};

// Signes astrologiques
const ZODIAC_SIGNS: Record<string, string> = {
  'Aries': 'Bélier',
  'Taurus': 'Taureau',
  'Gemini': 'Gémeaux',
  'Cancer': 'Cancer',
  'Leo': 'Lion',
  'Virgo': 'Vierge',
  'Libra': 'Balance',
  'Scorpio': 'Scorpion',
  'Sagittarius': 'Sagittaire',
  'Capricorn': 'Capricorne',
  'Aquarius': 'Verseau',
  'Pisces': 'Poissons',
};

// Mois de l'année
const MONTHS: Record<string, string> = {
  'January': 'Janvier',
  'February': 'Février',
  'March': 'Mars',
  'April': 'Avril',
  'May': 'Mai',
  'June': 'Juin',
  'July': 'Juillet',
  'August': 'Août',
  'September': 'Septembre',
  'October': 'Octobre',
  'November': 'Novembre',
  'December': 'Décembre',
};

/**
 * Traduit un signe astrologique de l'anglais vers le français
 */
export function translateZodiacSign(sign: string): string {
  return ZODIAC_SIGNS[sign] || sign;
}

/**
 * Traduit un mois de l'anglais vers le français
 */
export function translateMonth(month: string): string {
  return MONTHS[month] || month;
}

/**
 * Traduit toutes les planètes dans un texte
 * Ex: "Sun trine Moon" → "Soleil trine Lune"
 */
export function translatePlanetsInText(text: string): string {
  let result = text;

  Object.entries(PLANETS).forEach(([en, fr]) => {
    const regex = new RegExp(`\\b${en}\\b`, 'g');
    result = result.replace(regex, fr);
  });

  return result;
}

/**
 * Traduit tous les signes astrologiques dans un texte
 * Ex: "Aries in Sagittarius" → "Bélier in Sagittaire"
 */
export function translateZodiacInText(text: string): string {
  let result = text;

  Object.entries(ZODIAC_SIGNS).forEach(([en, fr]) => {
    // Remplacer avec word boundaries pour éviter les faux positifs
    const regex = new RegExp(`\\b${en}\\b`, 'g');
    result = result.replace(regex, fr);
  });

  return result;
}

/**
 * Traduit tous les mois dans un texte
 * Ex: "January 2026" → "Janvier 2026"
 */
export function translateMonthsInText(text: string): string {
  let result = text;

  Object.entries(MONTHS).forEach(([en, fr]) => {
    const regex = new RegExp(`\\b${en}\\b`, 'g');
    result = result.replace(regex, fr);
  });

  return result;
}

/**
 * Traduit toutes les références astrologiques dans un texte (mois + signes + planètes)
 */
export function translateAstrologyText(text: string): string {
  let result = text;
  result = translateMonthsInText(result);
  result = translatePlanetsInText(result);
  result = translateZodiacInText(result);
  return result;
}
