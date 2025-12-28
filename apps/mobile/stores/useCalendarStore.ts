import { create } from 'zustand';

interface CalendarState {
  calendarData: Record<string, any>; // Key: "YYYY-MM"
  lastFetch: Record<string, number>;
  isLoading: boolean;
  error: string | null;
  setCalendar: (month: string, data: any) => void;
  getCalendar: (month: string) => any | null;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  isStale: (month: string) => boolean;
  clear: () => void;
}

const TTL = 5 * 60 * 1000; // 5 minutes

export const useCalendarStore = create<CalendarState>((set, get) => ({
  calendarData: {},
  lastFetch: {},
  isLoading: false,
  error: null,

  setCalendar: (month, data) =>
    set((state) => ({
      calendarData: { ...state.calendarData, [month]: data },
      lastFetch: { ...state.lastFetch, [month]: Date.now() },
      error: null,
    })),

  getCalendar: (month) => {
    const state = get();
    return state.calendarData[month] || null;
  },

  setLoading: (loading) => set({ isLoading: loading }),

  setError: (error) => set({ error, isLoading: false }),

  isStale: (month) => {
    const state = get();
    const lastFetch = state.lastFetch[month];
    if (!lastFetch) return true;
    return Date.now() - lastFetch > TTL;
  },

  clear: () =>
    set({
      calendarData: {},
      lastFetch: {},
      error: null,
    }),
}));

