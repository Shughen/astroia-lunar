/**
 * Tests pour les helpers d'onboarding (isProfileComplete, etc.)
 */

import { isProfileComplete, type ProfileData } from '../utils/onboardingHelpers';

describe('isProfileComplete', () => {
  it('devrait retourner false si profileData est null', () => {
    expect(isProfileComplete(null)).toBe(false);
  });

  it('devrait retourner false si profileData est undefined', () => {
    expect(isProfileComplete(undefined)).toBe(false);
  });

  it('devrait retourner false si birthDate manque', () => {
    const profile: ProfileData = {
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthTime manque', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthTime est vide', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthPlace manque', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '12:00',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthPlace est vide', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '12:00',
      birthPlace: '',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthLatitude manque', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthLongitude manque', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthLatitude est NaN', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLatitude: NaN,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthLongitude est NaN', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: NaN,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthDate est une Date invalide', () => {
    const profile: ProfileData = {
      birthDate: new Date('invalid'),
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner false si birthDate est une string vide', () => {
    const profile: ProfileData = {
      birthDate: '' as any,
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });

  it('devrait retourner true si tous les champs requis sont présents et valides (Date object)', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(true);
  });

  it('devrait retourner true si tous les champs requis sont présents et valides (string date)', () => {
    const profile: ProfileData = {
      birthDate: '1990-01-15' as any,
      birthTime: '14:30',
      birthPlace: 'Lyon, France',
      birthLatitude: 45.7640,
      birthLongitude: 4.8357,
    };
    expect(isProfileComplete(profile)).toBe(true);
  });

  it('devrait retourner true même si name n\'est pas présent', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '12:00',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(true);
  });

  it('devrait accepter birthTime avec des espaces et les ignorer', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '  12:00  ',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    // Note: trim() est fait dans la fonction, mais "  12:00  ".trim() = "12:00" qui est valide
    expect(isProfileComplete(profile)).toBe(true);
  });

  it('devrait retourner false si birthTime ne contient que des espaces', () => {
    const profile: ProfileData = {
      birthDate: new Date('1990-01-15'),
      birthTime: '   ',
      birthPlace: 'Paris, France',
      birthLatitude: 48.8566,
      birthLongitude: 2.3522,
    };
    expect(isProfileComplete(profile)).toBe(false);
  });
});

