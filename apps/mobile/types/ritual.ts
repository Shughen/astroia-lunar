/**
 * Types pour la carte Rituel Quotidien
 */

export type MoonPhase =
  | 'New Moon'
  | 'Waxing Crescent'
  | 'First Quarter'
  | 'Waxing Gibbous'
  | 'Full Moon'
  | 'Waning Gibbous'
  | 'Last Quarter'
  | 'Waning Crescent';

export interface DailyRitualData {
  date: string; // YYYY-MM-DD
  moon: {
    phase: MoonPhase;
    sign: string; // "Aquarius", "Taurus", etc.
  };
  voc?: {
    is_active: boolean;
    end_at: string; // ISO timestamp
  };
}

export interface CachedRitualData {
  data: DailyRitualData;
  cached_at: number; // Timestamp
}

export interface VocStatus {
  now: {
    is_active: boolean;
    start_at: string;
    end_at: string;
  } | null;
  next: {
    start_at: string;
    end_at: string;
  } | null;
  upcoming: Array<{
    start_at: string;
    end_at: string;
  }>;
}
