/**
 * Test de vérification que Jest fonctionne correctement
 */

describe('Jest Setup', () => {
  it('should run tests successfully', () => {
    expect(true).toBe(true);
  });

  it('should have access to test utilities', () => {
    expect(jest).toBeDefined();
  });
});
