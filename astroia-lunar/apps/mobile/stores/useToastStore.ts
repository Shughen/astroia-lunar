/**
 * Store Zustand pour les toasts/snackbars
 * Affiche des messages temporaires non-bloquants
 */

import { create } from 'zustand';

export type ToastType = 'info' | 'success' | 'warning' | 'error';

export interface Toast {
  id: string;
  message: string;
  type: ToastType;
  duration: number; // ms
}

interface ToastState {
  toasts: Toast[];
  showToast: (message: string, type?: ToastType, duration?: number) => void;
  hideToast: (id: string) => void;
  clearAll: () => void;
}

// Durées par défaut selon le type
const DEFAULT_DURATIONS: Record<ToastType, number> = {
  info: 3000,
  success: 2500,
  warning: 4000,
  error: 5000,
};

export const useToastStore = create<ToastState>((set, get) => ({
  toasts: [],

  showToast: (message: string, type: ToastType = 'info', duration?: number) => {
    const id = `toast-${Date.now()}-${Math.random().toString(36).slice(2, 9)}`;
    const toastDuration = duration ?? DEFAULT_DURATIONS[type];

    const newToast: Toast = {
      id,
      message,
      type,
      duration: toastDuration,
    };

    set((state) => ({
      toasts: [...state.toasts, newToast],
    }));

    // Auto-dismiss après la durée
    setTimeout(() => {
      get().hideToast(id);
    }, toastDuration);
  },

  hideToast: (id: string) => {
    set((state) => ({
      toasts: state.toasts.filter((t) => t.id !== id),
    }));
  },

  clearAll: () => {
    set({ toasts: [] });
  },
}));
