/**
 * Utilitaires pour calculer le cycle lunaire
 */

const LUNAR_CYCLE_DAYS = 29.53059;

/**
 * Calcule le numéro de cycle lunaire actuel basé sur la date de naissance
 * 
 * Cycle 1 = première révolution après la naissance (0-29.5 jours)
 * Cycle 2 = deuxième révolution (29.5-59 jours)
 * etc.
 * 
 * @param birthDate Date de naissance au format ISO (YYYY-MM-DD) ou Date object
 * @returns Numéro de cycle (1, 2, 3, ...)
 */
export function calculateCurrentCycleNumber(birthDate: string | Date): number {
  const birth = typeof birthDate === 'string' ? new Date(birthDate) : birthDate;
  const now = new Date();
  
  // Différence en millisecondes
  const diffMs = now.getTime() - birth.getTime();
  const diffDays = diffMs / (1000 * 60 * 60 * 24);
  
  // Calculer le cycle (commence à 1)
  const cycleNumber = Math.floor(diffDays / LUNAR_CYCLE_DAYS) + 1;
  
  // S'assurer que le cycle est au moins 1
  return Math.max(1, cycleNumber);
}

/**
 * Calcule le numéro de cycle pour un mois donné (approximation)
 * Utile pour calculer le cycle d'un mois spécifique
 * 
 * @param birthDate Date de naissance au format ISO (YYYY-MM-DD) ou Date object
 * @param targetMonth Mois cible au format YYYY-MM ou Date object
 * @returns Numéro de cycle approximatif
 */
export function calculateCycleNumberForMonth(
  birthDate: string | Date,
  targetMonth: string | Date
): number {
  const birth = typeof birthDate === 'string' ? new Date(birthDate) : birthDate;
  const target = typeof targetMonth === 'string' 
    ? new Date(targetMonth + '-15') // Milieu du mois pour approximation
    : targetMonth;
  
  const diffMs = target.getTime() - birth.getTime();
  const diffDays = diffMs / (1000 * 60 * 60 * 24);
  
  const cycleNumber = Math.floor(diffDays / LUNAR_CYCLE_DAYS) + 1;
  
  return Math.max(1, cycleNumber);
}

