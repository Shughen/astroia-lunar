/**
 * Dictionnaires de traduction astrologique FR
 * Mapping EN → FR pour signes, planètes, aspects
 */

// Signes du zodiaque
export const SIGN_FR: Record<string, string> = {
  'aries': 'Bélier',
  'taurus': 'Taureau',
  'gemini': 'Gémeaux',
  'cancer': 'Cancer',
  'leo': 'Lion',
  'virgo': 'Vierge',
  'libra': 'Balance',
  'scorpio': 'Scorpion',
  'sagittarius': 'Sagittaire',
  'capricorn': 'Capricorne',
  'aquarius': 'Verseau',
  'pisces': 'Poissons',
};

// Planètes et points sensibles
export const PLANET_FR: Record<string, string> = {
  'sun': 'Soleil',
  'moon': 'Lune',
  'mercury': 'Mercure',
  'venus': 'Vénus',
  'mars': 'Mars',
  'jupiter': 'Jupiter',
  'saturn': 'Saturne',
  'uranus': 'Uranus',
  'neptune': 'Neptune',
  'pluto': 'Pluton',
  'chiron': 'Chiron',
  'lilith': 'Lilith',
  'blackmoon': 'Lilith',
  'black_moon': 'Lilith',
  // Nœuds lunaires
  'northnode': 'Nœud Nord',
  'north_node': 'Nœud Nord',
  'meannorthnode': 'Nœud Nord',
  'mean_north_node': 'Nœud Nord',
  'truenorthnode': 'Nœud Nord',
  'true_north_node': 'Nœud Nord',
  'southnode': 'Nœud Sud',
  'south_node': 'Nœud Sud',
  'meansouthnode': 'Nœud Sud',
  'mean_south_node': 'Nœud Sud',
  'truesouthnode': 'Nœud Sud',
  'true_south_node': 'Nœud Sud',
  // Points sensibles
  'mediumcoeli': 'Milieu du Ciel',
  'medium_coeli': 'Milieu du Ciel',
  'mc': 'Milieu du Ciel',
  'imumcoeli': 'Fond du Ciel',
  'imum_coeli': 'Fond du Ciel',
  'ic': 'Fond du Ciel',
  'partoffortune': 'Part de Fortune',
  'part_of_fortune': 'Part de Fortune',
  'pof': 'Part de Fortune',
  'vertex': 'Vertex',
};

// Aspects
export const ASPECT_FR: Record<string, string> = {
  'conjunction': 'Conjonction',
  'sextile': 'Sextile',
  'square': 'Carré',
  'trine': 'Trigone',
  'opposition': 'Opposition',
  'quincunx': 'Quinconce',
  'semisextile': 'Semi-sextile',
  'semi_sextile': 'Semi-sextile',
  'semisquare': 'Semi-carré',
  'semi_square': 'Semi-carré',
  'sesquisquare': 'Sesqui-carré',
  'sesqui_square': 'Sesqui-carré',
};
