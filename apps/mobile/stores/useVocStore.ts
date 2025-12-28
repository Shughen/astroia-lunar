import { create } from 'zustand';

interface VocState {
  vocData: any | null;
  lastFetch: number | null;
  isLoading: boolean;
  error: string | null;
  setVoc: (data: any) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  isStale: () => boolean;
  clear: () => void;
}

const TTL = 5 * 60 * 1000; // 5 minutes

export const useVocStore = create<VocState>((set, get) => ({
  vocData: null,
  lastFetch: null,
  isLoading: false,
  error: null,

  setVoc: (data) =>
    set({
      vocData: data,
      lastFetch: Date.now(),
      error: null,
    }),

  setLoading: (loading) => set({ isLoading: loading }),

  setError: (error) => set({ error, isLoading: false }),

  isStale: () => {
    const state = get();
    if (!state.lastFetch) return true;
    return Date.now() - state.lastFetch > TTL;
  },

  clear: () =>
    set({
      vocData: null,
      lastFetch: null,
      error: null,
    }),
}));

