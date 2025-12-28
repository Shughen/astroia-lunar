/**
 * Store Zustand pour l'authentification
 */

import { create } from 'zustand';

interface User {
  id: number;
  email: string;
  birth_date?: string;
  birth_time?: string;
  birth_place_name?: string;
  is_premium: boolean;
}

interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  setUser: (user: User | null) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,
  
  setUser: (user) => set({ user, isAuthenticated: !!user }),
  
  logout: () => set({ user: null, isAuthenticated: false }),
}));

