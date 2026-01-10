/**
 * Tests pour filterMajorAspectsV4
 * Valide les règles v4: types majeurs, orbe ≤6°, exclure Lilith
 */

import { filterMajorAspectsV4 } from '../natalChartUtils';

describe('filterMajorAspectsV4', () => {
  const mockAspects = [
    { planet1: 'sun', planet2: 'moon', type: 'conjunction', orb: 2.5 },      // ✅ v4
    { planet1: 'mercury', planet2: 'venus', type: 'sextile', orb: 1.0 },     // ❌ sextile (mineur)
    { planet1: 'mars', planet2: 'jupiter', type: 'trine', orb: 4.5 },        // ✅ v4
    { planet1: 'saturn', planet2: 'uranus', type: 'square', orb: 7.0 },      // ❌ orbe > 6°
    { planet1: 'neptune', planet2: 'pluto', type: 'opposition', orb: 5.8 },  // ✅ v4
    { planet1: 'mean_lilith', planet2: 'sun', type: 'conjunction', orb: 3.0 }, // ❌ Lilith
    { planet1: 'moon', planet2: 'chiron', type: 'trine', orb: 6.0 },         // ✅ v4 (orbe exactement 6)
    { planet1: 'venus', planet2: 'mars', type: 'quincunx', orb: 2.0 },       // ❌ quincunx (mineur)
  ];

  describe('v4 filtering (default)', () => {
    it('devrait retenir uniquement les aspects majeurs (conjunction, opposition, square, trine)', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      const types = filtered.map(a => a.type);
      expect(types.every(t => ['conjunction', 'opposition', 'square', 'trine'].includes(t))).toBe(true);
    });

    it('devrait exclure les sextiles même avec orbe faible', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      expect(filtered.find(a => a.type === 'sextile')).toBeUndefined();
    });

    it('devrait exclure les quincunx', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      expect(filtered.find(a => a.type === 'quincunx')).toBeUndefined();
    });

    it('devrait respecter orbe <= 6°', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      const allOrbsValid = filtered.every(a => Math.abs(a.orb) <= 6);
      expect(allOrbsValid).toBe(true);
    });

    it('devrait accepter orbe = 6° exactement', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      const orb6Aspect = filtered.find(a => Math.abs(a.orb) === 6);
      expect(orb6Aspect).toBeDefined();
      expect(orb6Aspect?.planet1).toBe('moon');
      expect(orb6Aspect?.planet2).toBe('chiron');
    });

    it('devrait exclure Lilith (mean_lilith)', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      const hasLilith = filtered.some(a =>
        a.planet1?.toLowerCase().includes('lilith') ||
        a.planet2?.toLowerCase().includes('lilith')
      );
      expect(hasLilith).toBe(false);
    });

    it('devrait trier par orbe croissant', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      for (let i = 1; i < filtered.length; i++) {
        const prevOrb = Math.abs(filtered[i - 1].orb);
        const currOrb = Math.abs(filtered[i].orb);
        expect(prevOrb).toBeLessThanOrEqual(currOrb);
      }
    });

    it('devrait retourner 4 aspects valides pour le jeu de test', () => {
      // Attendus: sun-moon (2.5°), mars-jupiter (4.5°), neptune-pluto (5.8°), moon-chiron (6.0°)
      const filtered = filterMajorAspectsV4(mockAspects, 4);

      expect(filtered).toHaveLength(4);
    });
  });

  describe('v2/v3 legacy (conserver tous)', () => {
    it('devrait conserver tous les aspects pour v2', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 2);

      expect(filtered.length).toBe(mockAspects.length);
    });

    it('devrait conserver tous les aspects pour v3', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 3);

      expect(filtered.length).toBe(mockAspects.length);
    });

    it('devrait trier par orbe même en v2', () => {
      const filtered = filterMajorAspectsV4(mockAspects, 2);

      for (let i = 1; i < filtered.length; i++) {
        const prevOrb = Math.abs(filtered[i - 1].orb);
        const currOrb = Math.abs(filtered[i].orb);
        expect(prevOrb).toBeLessThanOrEqual(currOrb);
      }
    });
  });

  describe('edge cases', () => {
    it('devrait gérer aspects vides', () => {
      const filtered = filterMajorAspectsV4([], 4);
      expect(filtered).toEqual([]);
    });

    it('devrait gérer orbe négatif (prendre valeur absolue)', () => {
      const negativeOrb = [
        { planet1: 'sun', planet2: 'moon', type: 'conjunction', orb: -3.5 }
      ];
      const filtered = filterMajorAspectsV4(negativeOrb, 4);

      expect(filtered).toHaveLength(1);
      expect(Math.abs(filtered[0].orb)).toBe(3.5);
    });

    it('devrait exclure Lilith avec variantes (lilith, mean_lilith, blackmoonlilith)', () => {
      const lilithVariants = [
        { planet1: 'lilith', planet2: 'sun', type: 'conjunction', orb: 2.0 },
        { planet1: 'mean_lilith', planet2: 'moon', type: 'trine', orb: 3.0 },
        { planet1: 'blackmoonlilith', planet2: 'venus', type: 'opposition', orb: 4.0 },
        { planet1: 'sun', planet2: 'Black_Moon_Lilith', type: 'square', orb: 5.0 },
      ];

      const filtered = filterMajorAspectsV4(lilithVariants, 4);

      expect(filtered).toHaveLength(0); // Tous exclus
    });
  });
});
