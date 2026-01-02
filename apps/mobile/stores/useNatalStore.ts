/**
 * Store Zustand pour le thème natal
 */

import { create } from 'zustand';

interface Planet {
  name: string;
  sign: string;
  degree: number;
  house: number;
  retrograde?: boolean;
}

interface House {
  number: number;
  sign: string;
  degree: number;
}

interface Aspect {
  planet1: string;
  planet2: string;
  type: string;
  angle: number;
  orb: number;
}

interface NatalChart {
  subject?: {
    name: string;
  };
  planets?: Planet[];
  houses?: House[];
  aspects?: Aspect[];
  sun_sign?: string;
  moon_sign?: string;
  ascendant?: string;
  raw_data?: unknown;
}

interface NatalState {
  chart: NatalChart | null;
  computed_at: number | null; // Timestamp du dernier calcul
  loading: boolean;
  isCalculating: boolean; // In-flight guard
  setChart: (chart: NatalChart | null) => void;
  setLoading: (loading: boolean) => void;
  clearChart: () => void;
  setIsCalculating: (isCalculating: boolean) => void;
  isCacheFresh: () => boolean; // Vérifie si le cache est valide (< 10 min)
}

const CACHE_TTL_MS = 10 * 60 * 1000; // 10 minutes

export const useNatalStore = create<NatalState>((set, get) => ({
  chart: null,
  computed_at: null,
  loading: false,
  isCalculating: false,

  setChart: (chart: NatalChart | null) => {
    const now = Date.now();
    console.log(`[NatalStore] setChart appelé, timestamp=${now}`);
    set({ chart, computed_at: chart ? now : null, loading: false, isCalculating: false });
  },

  setLoading: (loading: boolean) => set({ loading }),

  clearChart: () => {
    console.log('[NatalStore] clearChart appelé');
    set({ chart: null, computed_at: null, loading: false, isCalculating: false });
  },

  setIsCalculating: (isCalculating: boolean) => {
    console.log(`[NatalStore] setIsCalculating: ${isCalculating}`);
    set({ isCalculating });
  },

  isCacheFresh: () => {
    const { chart, computed_at } = get();
    if (!chart || !computed_at) {
      console.log('[NatalStore] Cache check: pas de chart ou pas de timestamp → MISS');
      return false;
    }

    const now = Date.now();
    const age = now - computed_at;
    const isFresh = age < CACHE_TTL_MS;

    if (isFresh) {
      const ageMin = Math.floor(age / 1000 / 60);
      console.log(`[NatalStore] Cache check: HIT (âge=${ageMin} min < 10 min)`);
    } else {
      const ageMin = Math.floor(age / 1000 / 60);
      console.log(`[NatalStore] Cache check: MISS (âge=${ageMin} min >= 10 min)`);
    }

    return isFresh;
  },
}));
