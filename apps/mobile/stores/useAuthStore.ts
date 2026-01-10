/**
 * Store Zustand pour l'authentification
 */

import { create } from 'zustand';
import type { AuthState } from '../types/stores';
import type { User } from '../types/api';

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,

  setUser: (user: User | null) => set({ user, isAuthenticated: !!user }),

  logout: () => set({ user: null, isAuthenticated: false }),
}));
