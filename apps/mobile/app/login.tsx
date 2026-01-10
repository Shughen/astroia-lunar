/**
 * Écran de connexion
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  Alert,
  ActivityIndicator,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { useAuthStore } from '../stores/useAuthStore';
import { auth } from '../services/api';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

export default function LoginScreen() {
  const router = useRouter();
  const { setUser } = useAuthStore();
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    if (!email || !password) {
      Alert.alert('Erreur', 'Merci de remplir tous les champs');
      return;
    }

    setLoading(true);
    try {
      await auth.login(email, password);
      const user = await auth.getMe();
      setUser(user);
      router.replace('/');
    } catch (error: any) {
      Alert.alert('Erreur', error.response?.data?.detail || 'Connexion échouée');
    } finally {
      setLoading(false);
    }
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>🌙 Connexion</Text>
        <Text style={styles.subtitle}>Bienvenue de retour !</Text>

        <View style={styles.form}>
          <TextInput
            style={styles.input}
            placeholder="Email"
            placeholderTextColor={colors.textMuted}
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
            autoCapitalize="none"
          />

          <TextInput
            style={styles.input}
            placeholder="Mot de passe"
            placeholderTextColor={colors.textMuted}
            value={password}
            onChangeText={setPassword}
            secureTextEntry
          />

          <TouchableOpacity
            style={[styles.button, loading && styles.buttonDisabled]}
            onPress={handleLogin}
            disabled={loading}
          >
            {loading ? (
              <ActivityIndicator color="#fff" />
            ) : (
              <Text style={styles.buttonText}>Se connecter</Text>
            )}
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.linkButton}
            onPress={() => router.push('/onboarding')}
          >
            <Text style={styles.linkText}>
              Pas encore de compte ? S'inscrire
            </Text>
          </TouchableOpacity>
        </View>
      </View>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    paddingHorizontal: spacing.xl,
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: spacing.xl,
  },
  form: {
    width: '100%',
  },
  input: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.md,
  },
  button: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginTop: spacing.lg,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonText: {
    ...fonts.button,
    color: colors.text,
  },
  linkButton: {
    marginTop: spacing.md,
    alignItems: 'center',
  },
  linkText: {
    ...fonts.body,
    color: colors.accent,
    textDecorationLine: 'underline',
  },
});

