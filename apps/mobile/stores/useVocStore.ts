/**
 * Store Zustand pour Void of Course
 */

import { create } from 'zustand';
import { lunaPack } from '../services/api';
import type { VocState, VoidOfCourseData } from '../types/stores';

export const useVocStore = create<VocState>((set) => ({
  currentVoc: null,
  isLoading: false,

  fetchCurrentVoc: async () => {
    set({ isLoading: true });
    try {
      const data = await lunaPack.getCurrentVoc();
      set({
        currentVoc: data,
        isLoading: false,
      });
    } catch (error) {
      console.error('[VocStore] Error fetching current VOC:', error);
      set({
        currentVoc: null,
        isLoading: false,
      });
    }
  },
}));
