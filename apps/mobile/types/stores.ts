/**
 * Types TypeScript pour les états Zustand
 */

import { User } from './api';

// Auth Store
export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  setUser: (user: User | null) => void;
  logout: () => void;
}

// Natal Store
export interface NatalState {
  birthDate: string | null;
  birthTime: string | null;
  birthPlace: string | null;
  latitude: number | null;
  longitude: number | null;
  setBirthData: (data: Partial<BirthData>) => Promise<void>;
  clearBirthData: () => Promise<void>;
}

export interface BirthData {
  birthDate: string;
  birthTime: string;
  birthPlace: string;
  latitude: number;
  longitude: number;
}

// Cycle Store
export interface CycleState {
  lastPeriodDate: Date | null;
  averageCycleLength: number;
  currentPhase: CyclePhase | null;
  setLastPeriod: (date: Date) => Promise<void>;
  setCycleLength: (days: number) => Promise<void>;
  calculateCurrentPhase: () => CyclePhase | null;
  clearCycleData: () => Promise<void>;
}

export type CyclePhase = 'menstrual' | 'follicular' | 'ovulation' | 'luteal';

// Calendar Store
export interface CalendarState {
  currentMonth: number;
  currentYear: number;
  setMonth: (month: number) => void;
  setYear: (year: number) => void;
}

// VOC Store
export interface VocState {
  currentVoc: VoidOfCourseData | null;
  isLoading: boolean;
  fetchCurrentVoc: () => Promise<void>;
}

export interface VoidOfCourseData {
  is_active: boolean;
  start_at: string;
  end_at: string;
}
