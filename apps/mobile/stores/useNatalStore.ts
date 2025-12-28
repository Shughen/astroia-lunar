/**
 * Store pour le thème natal
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
  raw_data?: any;
}

interface NatalState {
  chart: NatalChart | null;
  loading: boolean;
  setChart: (chart: NatalChart | null) => void;
  setLoading: (loading: boolean) => void;
  clearChart: () => void;
}

export const useNatalStore = create<NatalState>((set) => ({
  chart: null,
  loading: false,
  
  setChart: (chart) => set({ chart, loading: false }),
  
  setLoading: (loading) => set({ loading }),
  
  clearChart: () => set({ chart: null, loading: false }),
}));

