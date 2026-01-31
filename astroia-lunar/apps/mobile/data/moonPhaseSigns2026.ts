/**
 * Signes astrologiques des phases lunaires 2026
 * Source: ephemerides astronomiques
 * Format: 'YYYY-MM-DD' => signEmoji
 */

export const MOON_PHASE_SIGNS_2026: Record<string, string> = {
  // Janvier 2026
  '2026-01-03': '♋', // Pleine Lune - Cancer
  '2026-01-10': '♎', // Dernier Quartier - Balance
  '2026-01-18': '♑', // Nouvelle Lune - Capricorne
  '2026-01-26': '♉', // Premier Quartier - Taureau

  // Fevrier 2026
  '2026-02-01': '♋', // Pleine Lune - Cancer
  '2026-02-09': '♏', // Dernier Quartier - Scorpion
  '2026-02-17': '♒', // Nouvelle Lune - Verseau
  '2026-02-24': '♉', // Premier Quartier - Taureau

  // Mars 2026
  '2026-03-03': '♍', // Pleine Lune - Vierge
  '2026-03-11': '♐', // Dernier Quartier - Sagittaire
  '2026-03-19': '♓', // Nouvelle Lune - Poissons
  '2026-03-25': '♊', // Premier Quartier - Gemeaux

  // Avril 2026
  '2026-04-02': '♎', // Pleine Lune - Balance
  '2026-04-10': '♑', // Dernier Quartier - Capricorne
  '2026-04-17': '♈', // Nouvelle Lune - Belier
  '2026-04-24': '♌', // Premier Quartier - Lion

  // Mai 2026
  '2026-05-01': '♏', // Pleine Lune - Scorpion
  '2026-05-09': '♒', // Dernier Quartier - Verseau
  '2026-05-16': '♉', // Nouvelle Lune - Taureau
  '2026-05-23': '♌', // Premier Quartier - Lion
  '2026-05-31': '♐', // Pleine Lune - Sagittaire (micro)

  // Juin 2026
  '2026-06-08': '♓', // Dernier Quartier - Poissons
  '2026-06-15': '♊', // Nouvelle Lune - Gemeaux (super)
  '2026-06-21': '♍', // Premier Quartier - Vierge
  '2026-06-30': '♑', // Pleine Lune - Capricorne (micro)

  // Juillet 2026
  '2026-07-07': '♈', // Dernier Quartier - Belier
  '2026-07-14': '♋', // Nouvelle Lune - Cancer
  '2026-07-21': '♎', // Premier Quartier - Balance
  '2026-07-29': '♑', // Pleine Lune - Capricorne

  // Aout 2026
  '2026-08-06': '♉', // Dernier Quartier - Taureau
  '2026-08-12': '♌', // Nouvelle Lune - Lion
  '2026-08-20': '♏', // Premier Quartier - Scorpion
  '2026-08-28': '♓', // Pleine Lune - Poissons

  // Septembre 2026
  '2026-09-04': '♊', // Dernier Quartier - Gemeaux
  '2026-09-11': '♍', // Nouvelle Lune - Vierge
  '2026-09-18': '♐', // Premier Quartier - Sagittaire
  '2026-09-26': '♓', // Pleine Lune - Poissons

  // Octobre 2026
  '2026-10-03': '♋', // Dernier Quartier - Cancer
  '2026-10-10': '♎', // Nouvelle Lune - Balance
  '2026-10-18': '♑', // Premier Quartier - Capricorne
  '2026-10-26': '♈', // Pleine Lune - Belier

  // Novembre 2026
  '2026-11-01': '♋', // Dernier Quartier - Cancer
  '2026-11-09': '♏', // Nouvelle Lune - Scorpion
  '2026-11-17': '♒', // Premier Quartier - Verseau
  '2026-11-24': '♉', // Pleine Lune - Taureau

  // Decembre 2026
  '2026-12-01': '♍', // Dernier Quartier - Vierge
  '2026-12-09': '♐', // Nouvelle Lune - Sagittaire (micro)
  '2026-12-17': '♓', // Premier Quartier - Poissons
  '2026-12-24': '♋', // Pleine Lune - Cancer (super)
  '2026-12-30': '♍', // Dernier Quartier - Vierge
};

/**
 * Get zodiac sign emoji for a phase date
 */
export function getPhaseSign(dateKey: string): string | null {
  return MOON_PHASE_SIGNS_2026[dateKey] || null;
}
