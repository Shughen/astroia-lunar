/**
 * Design System Lunation
 * Couleurs, typographies, espacements
 */

export const colors = {
  // Backgrounds
  darkBg: ['#1a0b2e', '#2d1b4e'],
  cardBg: '#2a1a4e',
  
  // Accent
  accent: '#b794f6',
  accentDark: '#8b66d4',
  gold: '#ffd700',
  
  // Text
  text: '#ffffff',
  textMuted: '#a0a0b0',
  textDark: '#6a6a7a',
  
  // Semantic
  success: '#4ade80',
  error: '#f87171',
  warning: '#fbbf24',
  
  // Zodiac
  fire: '#ff6b6b',
  earth: '#8b7355',
  air: '#74c0fc',
  water: '#66d9ef',

  // Void of Course (VoC)
  vocWarning: '#f59e0b',
  vocBg: 'rgba(245, 158, 11, 0.2)',
  vocBorder: 'rgba(245, 158, 11, 0.4)',
} as const;

// Échelle de tailles typographiques (source unique)
const fontSizes = {
  xs: 12,
  sm: 14,
  md: 16,
  lg: 20,
  xl: 24,
  xxl: 32,
} as const;

export const fonts = {
  // Styles typographiques existants (conservés pour compatibilité)
  h1: {
    fontSize: 32,
    fontWeight: '700' as const,
    lineHeight: 40,
  },
  h2: {
    fontSize: 24,
    fontWeight: '700' as const,
    lineHeight: 32,
  },
  h3: {
    fontSize: 20,
    fontWeight: '600' as const,
    lineHeight: 28,
  },
  body: {
    fontSize: 16,
    fontWeight: '400' as const,
    lineHeight: 24,
  },
  bodySmall: {
    fontSize: 14,
    fontWeight: '400' as const,
    lineHeight: 20,
  },
  caption: {
    fontSize: 12,
    fontWeight: '400' as const,
    lineHeight: 16,
  },
  button: {
    fontSize: 16,
    fontWeight: '600' as const,
  },
  // Échelle de tailles (source unique)
  sizes: fontSizes,
  // Alias pour compatibilité avec fonts.size.*
  size: fontSizes,
} as const;

export const spacing = {
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  xxl: 48,
} as const;

export const borderRadius = {
  sm: 8,
  md: 16,
  lg: 24,
  full: 9999,
} as const;

export const shadows = {
  sm: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  md: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 8,
    elevation: 4,
  },
  lg: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.2,
    shadowRadius: 16,
    elevation: 8,
  },
} as const;

