/**
 * Types pour thème natal et interprétations
 */

export type NatalSubject =
  | 'sun'
  | 'moon'
  | 'ascendant'
  | 'midheaven'  // Milieu du Ciel (MC)
  | 'mercury'
  | 'venus'
  | 'mars'
  | 'jupiter'
  | 'saturn'
  | 'uranus'
  | 'neptune'
  | 'pluto'
  | 'chiron'
  | 'north_node'
  | 'south_node'
  | 'lilith';

export interface ChartPayload {
  subject_label: string;  // "Soleil", "Lune", etc.
  sign: string;           // "Bélier", "Taureau", etc.
  degree?: number;        // 0-30
  house?: number;         // 1-12
  ascendant_sign?: string; // Signe de l'Ascendant (contexte)
}

export interface NatalInterpretationRequest {
  chart_id: string;
  subject: NatalSubject;
  lang?: string;
  chart_payload: ChartPayload;
  force_refresh?: boolean;
}

export interface NatalInterpretationResponse {
  id?: string;
  text: string;
  cached: boolean;
  subject: NatalSubject;
  chart_id: string;
  version: number;
  created_at?: string;
}
