/**
 * Helpers pour formatage de dates
 */

/**
 * Formate une date en format français lisible
 * @param dateString - Date ISO string
 * @returns Date formatée (ex: "15 janvier 2025, 14:30")
 */
export function formatDate(dateString: string): string {
  const date = new Date(dateString);
  return date.toLocaleDateString('fr-FR', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
}

/**
 * Calcule le nombre de jours jusqu'à une date
 * @param dateString - Date ISO string
 * @returns Nombre de jours (positif = futur, négatif = passé)
 */
export function getDaysUntil(dateString: string): number {
  const date = new Date(dateString);
  const now = new Date();
  const diffTime = date.getTime() - now.getTime();
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  return diffDays;
}

/**
 * Formate une durée en texte lisible
 * @param days - Nombre de jours
 * @returns Texte formaté (ex: "dans 5 jours", "il y a 2 jours", "aujourd'hui")
 */
export function formatDaysUntil(days: number): string {
  if (days === 0) return "aujourd'hui";
  if (days === 1) return 'demain';
  if (days === -1) return 'hier';
  if (days > 0) return `dans ${days} jour${days > 1 ? 's' : ''}`;
  return `il y a ${Math.abs(days)} jour${Math.abs(days) > 1 ? 's' : ''}`;
}

/**
 * Formate une date en YYYY-MM-DD en heure locale (pas UTC!)
 *
 * IMPORTANT: N'utilise PAS toISOString() car cela convertit en UTC
 * et peut soustraire un jour selon la timezone.
 *
 * @param date - Objet Date
 * @returns Date formatée YYYY-MM-DD en heure locale
 *
 * @example
 * // Si l'utilisateur sélectionne 09/02/2001 à Paris (UTC+1):
 * // toISOString() donnerait "2001-02-08T23:00:00.000Z" ❌
 * // formatDateLocal() donne "2001-02-09" ✅
 */
export function formatDateLocal(date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}
