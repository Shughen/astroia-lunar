/**
 * Store pour gérer l'état de reset des données utilisateur
 * Empêche le routing de se déclencher pendant un reset atomique
 */

import { create } from 'zustand';

interface ResetState {
  isResetting: boolean;
  setIsResetting: (value: boolean) => void;
}

export const useResetStore = create<ResetState>((set) => ({
  isResetting: false,
  setIsResetting: (value: boolean) => set({ isResetting: value }),
}));

