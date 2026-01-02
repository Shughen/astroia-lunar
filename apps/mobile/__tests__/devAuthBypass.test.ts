/**
 * Tests pour devAuthBypass utilities
 */

import { getDevUserIdHeaderValue, resetWarningFlag } from '../utils/devAuthBypass';

describe('getDevUserIdHeaderValue', () => {
  beforeEach(() => {
    // Reset console.warn mock et flag de warning avant chaque test
    jest.clearAllMocks();
    resetWarningFlag();
  });

  it('devrait retourner "1" pour un entier valide', () => {
    expect(getDevUserIdHeaderValue('1')).toBe('1');
  });

  it('devrait normaliser "001" en "1"', () => {
    expect(getDevUserIdHeaderValue('001')).toBe('1');
  });

  it('devrait normaliser "123" en "123"', () => {
    expect(getDevUserIdHeaderValue('123')).toBe('123');
  });

  it('devrait retourner null pour un UUID', () => {
    const result = getDevUserIdHeaderValue('550e8400-e29b-41d4-a716-446655440000');
    expect(result).toBeNull();
  });

  it('devrait retourner null pour undefined', () => {
    expect(getDevUserIdHeaderValue(undefined)).toBeNull();
  });

  it('devrait retourner null pour une string vide', () => {
    expect(getDevUserIdHeaderValue('')).toBeNull();
    expect(getDevUserIdHeaderValue('   ')).toBeNull();
  });

  it('devrait retourner null pour une string non-numérique', () => {
    expect(getDevUserIdHeaderValue('abc')).toBeNull();
    expect(getDevUserIdHeaderValue('1.5')).toBeNull();
    expect(getDevUserIdHeaderValue('1a')).toBeNull();
  });

  it('devrait retourner null pour un nombre négatif', () => {
    expect(getDevUserIdHeaderValue('-1')).toBeNull();
  });

  it('devrait retourner null pour zéro', () => {
    expect(getDevUserIdHeaderValue('0')).toBeNull();
  });

  it('devrait logger un warning une seule fois pour valeur invalide', () => {
    const consoleSpy = jest.spyOn(console, 'warn').mockImplementation(() => {});
    
    // Premier appel avec UUID
    getDevUserIdHeaderValue('550e8400-e29b-41d4-a716-446655440000');
    expect(consoleSpy).toHaveBeenCalledTimes(1);
    
    // Deuxième appel avec autre valeur invalide
    getDevUserIdHeaderValue('abc');
    // Le warning ne devrait PAS être appelé une deuxième fois
    expect(consoleSpy).toHaveBeenCalledTimes(1);
    
    consoleSpy.mockRestore();
  });

  it('ne devrait pas logger de warning pour valeurs valides', () => {
    const consoleSpy = jest.spyOn(console, 'warn').mockImplementation(() => {});
    
    getDevUserIdHeaderValue('1');
    getDevUserIdHeaderValue('123');
    
    expect(consoleSpy).not.toHaveBeenCalled();
    
    consoleSpy.mockRestore();
  });
});

