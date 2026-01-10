/**
 * Store Zustand pour le calendrier lunaire
 */

import { create } from 'zustand';
import type { CalendarState } from '../types/stores';

const currentDate = new Date();

export const useCalendarStore = create<CalendarState>((set) => ({
  currentMonth: currentDate.getMonth() + 1,
  currentYear: currentDate.getFullYear(),

  setMonth: (month: number) => set({ currentMonth: month }),

  setYear: (year: number) => set({ currentYear: year }),
}));
