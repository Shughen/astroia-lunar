/**
 * Types TypeScript pour les réponses de l'API
 */

// Auth
export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export interface User {
  id: number;
  email: string;
  birth_date?: string;
  birth_time?: string;
  birth_place_name?: string;
  is_premium: boolean;
}

// Natal Chart
export interface NatalChartResponse {
  birth_date: string;
  birth_time: string;
  birth_place_name: string;
  latitude: number;
  longitude: number;
  planets: Planet[];
  houses: House[];
  ascendant: string;
  midheaven: string;
}

export interface Planet {
  name: string;
  sign: string;
  degree: number;
  retrograde: boolean;
  house?: number;
}

export interface House {
  number: number;
  sign: string;
  degree: number;
}

// Lunar Returns
export interface LunarReturn {
  id: string;
  return_date: string;
  moon_sign?: string;
  lunar_ascendant?: string;
  moon_house?: string;
  aspects?: Aspect[];
  interpretation?: string;
}

export interface Aspect {
  planet_1?: string;
  planet_2?: string;
  planet1?: string;
  planet2?: string;
  type?: string;
  aspect_type?: string;
  orb?: number;
}

// Aspect v4 enrichi avec explications pédagogiques (backend v4)
export interface AspectV4 {
  id: string;
  planet1: string;
  planet2: string;
  type: string;
  orb: number;
  expected_angle: 0 | 90 | 120 | 180;
  actual_angle?: number;
  delta_to_exact?: number;
  placements: {
    planet1: {
      sign: string;
      house?: number;
    };
    planet2: {
      sign: string;
      house?: number;
    };
  };
  copy?: {
    summary: string;
    why: string[];
    manifestation: string;
    advice?: string;
    shadow?: string;  // v5: section "Attention" (piège à éviter)
  };
}

// Transits
export interface TransitResponse {
  provider: string;
  kind: string;
  data: {
    aspects: Aspect[];
  };
}

export interface TransitPayload {
  birth_date: string;
  transit_date: string;
}

// Calendar
export interface CalendarMonth {
  year: number;
  month: number;
  days: CalendarDay[];
}

export interface CalendarDay {
  date: string;
  moon_phase: string;
  void_of_course?: boolean;
}

// Void of Course
export interface VoidOfCourse {
  is_active: boolean;
  start_at: string;
  end_at: string;
}
