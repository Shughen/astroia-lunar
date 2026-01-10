/**
 * Logger utility (Phase 1.6)
 * Wraps console logging to only output in development mode
 */

export const logger = {
  log: (...args: any[]) => {
    if (__DEV__) {
      console.log(...args);
    }
  },

  error: (...args: any[]) => {
    // Always show errors, even in production
    console.error(...args);
  },

  warn: (...args: any[]) => {
    if (__DEV__) {
      console.warn(...args);
    }
  },

  info: (...args: any[]) => {
    if (__DEV__) {
      console.info(...args);
    }
  },
};
