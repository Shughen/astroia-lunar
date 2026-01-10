/**
 * Messages du Climat Lunaire
 * 12 maisons × 3 tons = 36 messages
 */

export type ClimateTone = 'harmonieux' | 'tendu' | 'neutre';

export interface ClimateMessage {
  theme: string; // Ex: "Relations", "Carrière"
  message: string; // 2-3 lignes max
}

// Messages par maison activée
export const CLIMATE_MESSAGES: Record<number, Record<ClimateTone, ClimateMessage>> = {
  // Maison 1 - Identité, apparence
  1: {
    harmonieux: {
      theme: 'Rayonnement',
      message: 'La Lune éclaire ton identité. Journée propice pour affirmer qui tu es et initier ce qui te tient à cœur.',
    },
    tendu: {
      theme: 'Ajustement',
      message: 'La Lune bouscule ton image. Moment d\'ajustement personnel, sois patient avec toi-même.',
    },
    neutre: {
      theme: 'Présence',
      message: 'La Lune active ton identité. Journée pour te reconnecter à tes besoins essentiels.',
    },
  },

  // Maison 2 - Ressources, valeurs
  2: {
    harmonieux: {
      theme: 'Stabilité',
      message: 'La Lune sécurise tes ressources. Moment favorable pour gérer tes finances ou clarifier tes valeurs.',
    },
    tendu: {
      theme: 'Révision',
      message: 'La Lune questionne tes priorités. Temps de réajuster ton rapport à l\'argent ou tes possessions.',
    },
    neutre: {
      theme: 'Ancrage',
      message: 'La Lune traverse ta zone des ressources. Journée pour observer ce qui compte vraiment.',
    },
  },

  // Maison 3 - Communication, apprentissage
  3: {
    harmonieux: {
      theme: 'Échanges',
      message: 'La Lune fluidifie tes échanges. Journée idéale pour dialoguer, apprendre ou partager tes idées.',
    },
    tendu: {
      theme: 'Malentendus',
      message: 'La Lune complique la communication. Prends le temps de clarifier avant de réagir.',
    },
    neutre: {
      theme: 'Curiosité',
      message: 'La Lune stimule ton mental. Moment pour lire, découvrir ou échanger avec ton entourage.',
    },
  },

  // Maison 4 - Foyer, racines
  4: {
    harmonieux: {
      theme: 'Cocooning',
      message: 'La Lune réconforte ton foyer. Journée propice pour te ressourcer chez toi ou avec ta famille.',
    },
    tendu: {
      theme: 'Remous',
      message: 'La Lune agite ton espace intime. Accueille les émotions familiales sans te laisser submerger.',
    },
    neutre: {
      theme: 'Racines',
      message: 'La Lune éclaire ton foyer. Temps pour honorer tes besoins de sécurité et d\'appartenance.',
    },
  },

  // Maison 5 - Créativité, plaisirs
  5: {
    harmonieux: {
      theme: 'Joie',
      message: 'La Lune illumine ta créativité. Journée pour jouer, créer ou simplement te faire plaisir.',
    },
    tendu: {
      theme: 'Blocage',
      message: 'La Lune freine ton expression. Moment pour observer tes résistances sans forcer.',
    },
    neutre: {
      theme: 'Expression',
      message: 'La Lune active ta zone créative. Journée pour explorer ce qui te fait vibrer.',
    },
  },

  // Maison 6 - Quotidien, santé
  6: {
    harmonieux: {
      theme: 'Organisation',
      message: 'La Lune structure ton quotidien. Moment idéal pour prendre soin de toi et optimiser ta routine.',
    },
    tendu: {
      theme: 'Surcharge',
      message: 'La Lune charge ton emploi du temps. Priorise l\'essentiel et délègue si possible.',
    },
    neutre: {
      theme: 'Rituel',
      message: 'La Lune traverse ta zone santé. Temps pour affiner tes habitudes et te recentrer.',
    },
  },

  // Maison 7 - Relations, partenariats
  7: {
    harmonieux: {
      theme: 'Harmonie',
      message: 'La Lune adoucit tes relations. Moment favorable pour dialoguer, collaborer ou simplement être avec l\'autre.',
    },
    tendu: {
      theme: 'Tensions',
      message: 'La Lune révèle des frictions relationnelles. Accueille ce qui émerge sans jugement.',
    },
    neutre: {
      theme: 'Miroir',
      message: 'La Lune active tes partenariats. Journée pour observer la qualité de tes liens.',
    },
  },

  // Maison 8 - Transformation, profondeur
  8: {
    harmonieux: {
      theme: 'Libération',
      message: 'La Lune soutient ta transformation. Journée propice pour lâcher ce qui ne te sert plus.',
    },
    tendu: {
      theme: 'Intensité',
      message: 'La Lune remue des émotions profondes. Accueille cette intensité avec douceur.',
    },
    neutre: {
      theme: 'Profondeur',
      message: 'La Lune plonge dans ton inconscient. Moment pour explorer tes parts d\'ombre.',
    },
  },

  // Maison 9 - Expansion, philosophie
  9: {
    harmonieux: {
      theme: 'Inspiration',
      message: 'La Lune élargit ton horizon. Journée idéale pour voyager (physiquement ou mentalement) ou apprendre.',
    },
    tendu: {
      theme: 'Doutes',
      message: 'La Lune questionne tes croyances. Moment pour réviser tes certitudes avec ouverture.',
    },
    neutre: {
      theme: 'Quête',
      message: 'La Lune active ta soif de sens. Temps pour explorer ce qui donne du souffle à ta vie.',
    },
  },

  // Maison 10 - Carrière, accomplissement
  10: {
    harmonieux: {
      theme: 'Accomplissement',
      message: 'La Lune soutient tes ambitions. Journée pour avancer concrètement sur un projet professionnel.',
    },
    tendu: {
      theme: 'Pression',
      message: 'La Lune challenge ta direction. Moment pour questionner tes objectifs sans te juger.',
    },
    neutre: {
      theme: 'Visibilité',
      message: 'La Lune éclaire ta zone professionnelle. Temps pour structurer et planifier.',
    },
  },

  // Maison 11 - Amis, projets
  11: {
    harmonieux: {
      theme: 'Connexion',
      message: 'La Lune tisse des liens. Journée propice pour retrouver tes amis ou rejoindre un collectif.',
    },
    tendu: {
      theme: 'Décalage',
      message: 'La Lune crée des distances amicales. Respecte ton besoin de solitude sans culpabiliser.',
    },
    neutre: {
      theme: 'Réseau',
      message: 'La Lune active tes amitiés. Moment pour partager tes rêves avec ceux qui te comprennent.',
    },
  },

  // Maison 12 - Spiritualité, retrait
  12: {
    harmonieux: {
      theme: 'Sérénité',
      message: 'La Lune t\'invite au repos. Journée pour ralentir, méditer ou simplement ne rien faire.',
    },
    tendu: {
      theme: 'Confusion',
      message: 'La Lune brouille tes repères. Accueille cette brume sans chercher à tout contrôler.',
    },
    neutre: {
      theme: 'Introspection',
      message: 'La Lune traverse ton monde intérieur. Temps pour te retirer et écouter ton intuition.',
    },
  },
};

// Messages fallback (si pas de thème natal complet)
export const FALLBACK_MESSAGES = {
  // Fallback basé uniquement sur la phase lunaire
  phase: {
    'Nouvelle Lune': {
      theme: 'Intentions',
      message: 'Nouvelle Lune : le ciel t\'invite à ralentir et planter des graines pour le cycle à venir.',
    },
    'Premier Croissant': {
      theme: 'Action',
      message: 'Premier Croissant : moment pour agir sur tes intentions et donner forme à tes projets.',
    },
    'Premier Quartier': {
      theme: 'Décision',
      message: 'Premier Quartier : temps de faire des choix et ajuster ta trajectoire.',
    },
    'Lune Gibbeuse': {
      theme: 'Peaufinage',
      message: 'Lune Gibbeuse : affine tes actions avant la pleine visibilité.',
    },
    'Pleine Lune': {
      theme: 'Révélation',
      message: 'Pleine Lune : ce qui a grandi se révèle. Accueille ce qui émerge avec conscience.',
    },
    'Lune Disseminante': {
      theme: 'Partage',
      message: 'Lune Disseminante : moment pour partager ce que tu as appris.',
    },
    'Dernier Quartier': {
      theme: 'Libération',
      message: 'Dernier Quartier : temps de lâcher ce qui ne sert plus pour faire de la place.',
    },
    'Dernier Croissant': {
      theme: 'Recueillement',
      message: 'Dernier Croissant : le cycle se ferme. Honore ce qui a été et prépare-toi au renouveau.',
    },
  },
};
