/**
 * i18n configuration for Lunation
 *
 * Initializes i18next with French and English translations.
 * Default language: French (fr)
 */

import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

import frTranslations from './fr.json';
import enTranslations from './en.json';

i18n
  .use(initReactI18next)
  .init({
    compatibilityJSON: 'v4', // Required for proper JSON parsing in React Native
    resources: {
      fr: {
        translation: frTranslations,
      },
      en: {
        translation: enTranslations,
      },
    },
    lng: 'fr', // Default language
    fallbackLng: 'fr',
    interpolation: {
      escapeValue: false, // React already escapes values
    },
    react: {
      useSuspense: false, // Disable suspense for React Native compatibility
    },
  });

export default i18n;
