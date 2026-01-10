/**
 * Store Zustand pour la gestion des cycles menstruels
 */

import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { menstrualCycle } from '../services/api';

export interface MenstrualCycle {
  id: number;
  user_id: number;
  start_date: string;
  end_date: string | null;
  cycle_length: number | null;
  period_length: number | null;
  current_phase: string | null;
  cycle_day: number | null;
  notes: string | null;
  symptoms: string | null;
  created_at: string;
  updated_at: string | null;
}

export interface CurrentCycleResponse {
  cycle: MenstrualCycle | null;
  phase: string | null;
  day: number | null;
  next_period_prediction: string | null;
  average_cycle_length: number | null;
}

export interface CycleCorrelation {
  cycle: {
    phase: string;
    day: number;
    start_date: string;
  };
  lunar: {
    moon_sign: string | null;
    lunar_ascendant: string | null;
    moon_house: number | null;
  };
  energy: {
    total_energy: number;
    base_energy: number;
    lunar_bonus: number;
    element_bonus: number;
  };
  recommendations: {
    activities: string[];
    wellness: string[];
    nutrition: string[];
    rest: boolean;
  };
  insights: string[];
}

interface CycleStore {
  currentCycle: CurrentCycleResponse | null;
  cycles: MenstrualCycle[];
  correlation: CycleCorrelation | null;
  isLoading: boolean;
  error: string | null;
  lastFetch: number | null;
  
  // Actions
  fetchCurrentCycle: () => Promise<void>;
  fetchHistory: () => Promise<void>;
  fetchCorrelation: () => Promise<void>;
  startCycle: (startDate: Date, cycleLength?: number, periodLength?: number) => Promise<void>;
  endCycle: (cycleId: number, endDate: Date) => Promise<void>;
  clear: () => void;
  isStale: () => boolean;
}

const TTL = 5 * 60 * 1000; // 5 minutes

export const useCycleStore = create<CycleStore>((set, get) => ({
  currentCycle: null,
  cycles: [],
  correlation: null,
  isLoading: false,
  error: null,
  lastFetch: null,

  fetchCurrentCycle: async () => {
    const state = get();
    if (state.isStale() || !state.currentCycle) {
      set({ isLoading: true, error: null });
      try {
        const response = await menstrualCycle.getCurrent();
        set({
          currentCycle: response,
          lastFetch: Date.now(),
          isLoading: false,
        });
      } catch (error: any) {
        set({
          error: error.response?.data?.detail || 'Erreur lors du chargement du cycle',
          isLoading: false,
        });
      }
    }
  },

  fetchHistory: async () => {
    set({ isLoading: true, error: null });
    try {
      const response = await menstrualCycle.getHistory(12);
      set({
        cycles: response,
        isLoading: false,
      });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Erreur lors du chargement de l\'historique',
        isLoading: false,
      });
    }
  },

  fetchCorrelation: async () => {
    set({ isLoading: true, error: null });
    try {
      const response = await menstrualCycle.getCorrelation();
      set({
        correlation: response,
        isLoading: false,
      });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Erreur lors du calcul de la corrélation',
        isLoading: false,
      });
    }
  },

  startCycle: async (startDate: Date, cycleLength?: number, periodLength?: number) => {
    set({ isLoading: true, error: null });
    try {
      await menstrualCycle.start({
        start_date: startDate.toISOString(),
        cycle_length: cycleLength,
        period_length: periodLength,
      } as any);
      // Rafraîchir le cycle actuel
      await get().fetchCurrentCycle();
      await get().fetchCorrelation();
      set({ isLoading: false });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Erreur lors du démarrage du cycle',
        isLoading: false,
      });
      throw error;
    }
  },

  endCycle: async (cycleId: number, endDate: Date) => {
    set({ isLoading: true, error: null });
    try {
      await menstrualCycle.update(cycleId, {
        end_date: endDate.toISOString(),
      } as any);
      // Rafraîchir
      await get().fetchCurrentCycle();
      await get().fetchHistory();
      set({ isLoading: false });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Erreur lors de la fin du cycle',
        isLoading: false,
      });
      throw error;
    }
  },

  clear: () => {
    set({
      currentCycle: null,
      cycles: [],
      correlation: null,
      error: null,
      lastFetch: null,
    });
  },

  isStale: () => {
    const { lastFetch } = get();
    if (!lastFetch) return true;
    return Date.now() - lastFetch > TTL;
  },
}));

