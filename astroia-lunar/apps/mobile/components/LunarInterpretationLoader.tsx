import React, { useEffect, useRef } from 'react';
import { View, Text, StyleSheet, Animated, Easing } from 'react-native';

interface LunarInterpretationLoaderProps {
  message?: string;
}

export default function LunarInterpretationLoader({
  message = "Génération de ton interprétation lunaire..."
}: LunarInterpretationLoaderProps) {
  // Animation pour le sablier (rotation)
  const rotateAnim = useRef(new Animated.Value(0)).current;

  // Animation pour les étoiles scintillantes
  const sparkleAnim = useRef(new Animated.Value(0)).current;

  // Animation pour la barre de progression (sans native driver pour width)
  const progressAnim = useRef(new Animated.Value(0)).current;

  // Animation pour les points de chargement (...)
  const dotsAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    // Rotation du sablier (flip toutes les 2 secondes)
    Animated.loop(
      Animated.sequence([
        Animated.timing(rotateAnim, {
          toValue: 1,
          duration: 1000,
          easing: Easing.bezier(0.4, 0.0, 0.2, 1),
          useNativeDriver: true,
        }),
        Animated.delay(1000),
        Animated.timing(rotateAnim, {
          toValue: 0,
          duration: 1000,
          easing: Easing.bezier(0.4, 0.0, 0.2, 1),
          useNativeDriver: true,
        }),
        Animated.delay(1000),
      ])
    ).start();

    // Scintillement des étoiles
    Animated.loop(
      Animated.sequence([
        Animated.timing(sparkleAnim, {
          toValue: 1,
          duration: 1500,
          easing: Easing.inOut(Easing.ease),
          useNativeDriver: true,
        }),
        Animated.timing(sparkleAnim, {
          toValue: 0,
          duration: 1500,
          easing: Easing.inOut(Easing.ease),
          useNativeDriver: true,
        }),
      ])
    ).start();

    // Animation barre de progression (va-et-vient)
    Animated.loop(
      Animated.sequence([
        Animated.timing(progressAnim, {
          toValue: 1,
          duration: 2000,
          easing: Easing.inOut(Easing.ease),
          useNativeDriver: false,  // width nécessite native driver false
        }),
        Animated.timing(progressAnim, {
          toValue: 0,
          duration: 2000,
          easing: Easing.inOut(Easing.ease),
          useNativeDriver: false,
        }),
      ])
    ).start();

    // Animation des points (...)
    Animated.loop(
      Animated.sequence([
        Animated.timing(dotsAnim, {
          toValue: 1,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.timing(dotsAnim, {
          toValue: 2,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.timing(dotsAnim, {
          toValue: 3,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.timing(dotsAnim, {
          toValue: 0,
          duration: 200,
          useNativeDriver: true,
        }),
      ])
    ).start();
  }, []);

  const rotate = rotateAnim.interpolate({
    inputRange: [0, 1],
    outputRange: ['0deg', '180deg'],
  });

  const sparkleOpacity = sparkleAnim.interpolate({
    inputRange: [0, 1],
    outputRange: [0.3, 1],
  });

  const sparkleScale = sparkleAnim.interpolate({
    inputRange: [0, 1],
    outputRange: [0.8, 1.2],
  });

  // Affichage conditionnel des points
  const getDots = () => {
    const numDots = Math.floor(dotsAnim._value);
    return '.'.repeat(numDots);
  };

  return (
    <View style={styles.container}>
      {/* Étoiles décoratives */}
      <View style={styles.starsContainer}>
        <Animated.Text
          style={[
            styles.star,
            styles.starTopLeft,
            {
              opacity: sparkleOpacity,
              transform: [{ scale: sparkleScale }]
            }
          ]}
        >
          ✨
        </Animated.Text>
        <Animated.Text
          style={[
            styles.star,
            styles.starTopRight,
            {
              opacity: sparkleOpacity,
              transform: [{ scale: sparkleScale }]
            }
          ]}
        >
          ⭐
        </Animated.Text>
        <Animated.Text
          style={[
            styles.star,
            styles.starBottomLeft,
            {
              opacity: sparkleOpacity,
              transform: [{ scale: sparkleScale }]
            }
          ]}
        >
          🌟
        </Animated.Text>
      </View>

      {/* Sablier animé */}
      <Animated.View
        style={[
          styles.hourglassContainer,
          { transform: [{ rotate }] }
        ]}
      >
        <Text style={styles.hourglass}>⏳</Text>
      </Animated.View>

      {/* Lune décorative */}
      <Text style={styles.moonIcon}>🌙</Text>

      {/* Message de chargement */}
      <View style={styles.textContainer}>
        <Text style={styles.mainText}>{message}</Text>
        <Animated.Text style={styles.dotsText}>
          {getDots()}
        </Animated.Text>
      </View>

      {/* Barre de progression indéterminée */}
      <View style={styles.progressBarContainer}>
        <View style={styles.progressBarBackground}>
          <Animated.View
            style={[
              styles.progressBarFill,
              {
                width: progressAnim.interpolate({
                  inputRange: [0, 1],
                  outputRange: ['30%', '70%'],
                })
              }
            ]}
          />
        </View>
      </View>

      {/* Texte secondaire */}
      <Text style={styles.secondaryText}>
        Claude Opus 4.5 analyse ton cycle lunaire
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0A0E27',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  starsContainer: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
  },
  star: {
    position: 'absolute',
    fontSize: 24,
  },
  starTopLeft: {
    top: 100,
    left: 40,
  },
  starTopRight: {
    top: 120,
    right: 50,
  },
  starBottomLeft: {
    bottom: 200,
    left: 60,
  },
  hourglassContainer: {
    marginBottom: 20,
  },
  hourglass: {
    fontSize: 80,
    textAlign: 'center',
  },
  moonIcon: {
    fontSize: 40,
    marginBottom: 24,
    textAlign: 'center',
  },
  textContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 32,
  },
  mainText: {
    fontSize: 18,
    color: '#FFFFFF',
    fontWeight: '600',
    textAlign: 'center',
  },
  dotsText: {
    fontSize: 18,
    color: '#8B7BF7',
    fontWeight: '600',
    width: 30,
    textAlign: 'left',
  },
  progressBarContainer: {
    width: '100%',
    maxWidth: 300,
    marginBottom: 16,
  },
  progressBarBackground: {
    height: 6,
    backgroundColor: '#2D3561',
    borderRadius: 3,
    overflow: 'hidden',
  },
  progressBarFill: {
    height: '100%',
    backgroundColor: '#8B7BF7',
    borderRadius: 3,
  },
  secondaryText: {
    fontSize: 14,
    color: '#A0A0B0',
    textAlign: 'center',
    marginTop: 8,
  },
});
