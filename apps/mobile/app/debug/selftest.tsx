/**
 * Page de Self-Test pour le flux d'authentification
 * Route non liée à la navigation principale, accessible manuellement
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { auth, health, getApiUrl } from '../../services/api';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

interface TestResult {
  step: string;
  status: 'pending' | 'running' | 'success' | 'error';
  details: string;
}

export default function SelfTestScreen() {
  const [running, setRunning] = useState(false);
  const [results, setResults] = useState<TestResult[]>([]);
  const [token, setToken] = useState<string>('');

  const updateResult = (step: string, status: TestResult['status'], details: string) => {
    setResults(prev => {
      const existing = prev.find(r => r.step === step);
      if (existing) {
        return prev.map(r => r.step === step ? { step, status, details } : r);
      }
      return [...prev, { step, status, details }];
    });
  };

  const runTests = async () => {
    setRunning(true);
    setResults([]);
    setToken('');

    const testEmail = `test-${Date.now()}@selftest.local`;
    const testPassword = 'test123456';

    try {
      // Test 1: Health Check
      updateResult('Health Check', 'running', 'Testing /health...');
      try {
        const healthResponse = await health.check();
        if (healthResponse.status === 'healthy') {
          updateResult('Health Check', 'success', `API OK: ${JSON.stringify(healthResponse)}`);
        } else {
          updateResult('Health Check', 'error', `Status: ${healthResponse.status}`);
        }
      } catch (error: any) {
        updateResult('Health Check', 'error', error.message || 'Network error');
      }

      // Test 2: Register
      updateResult('Register', 'running', `Creating user: ${testEmail}...`);
      try {
        // Préparer les données de naissance avec types corrects
        const birthData = {
          birth_date: '1990-01-01',
          birth_time: '12:00',
          birth_latitude: 48.8566, // Float, pas string
          birth_longitude: 2.3522, // Float, pas string
          birth_place_name: 'Paris',
          birth_timezone: 'Europe/Paris',
        };

        // Logger le payload (sans password)
        const payloadForLog = { ...birthData, email: testEmail, password: '***' };
        console.log('[SELFTEST] Register payload:', JSON.stringify(payloadForLog, null, 2));
        console.log('[SELFTEST] Register endpoint: POST /api/auth/register');

        const registerResponse = await auth.register(
          testEmail,
          testPassword,
          birthData
        );
        
        if (registerResponse.access_token) {
          setToken(registerResponse.access_token);
          updateResult('Register', 'success', `Token: ${registerResponse.access_token.substring(0, 30)}...`);
        } else {
          updateResult('Register', 'error', 'No token received');
        }
      } catch (error: any) {
        // Logger les détails de l'erreur
        const errorStatus = error.response?.status;
        const errorData = error.response?.data;
        const errorMessage = error.message || 'Failed';
        
        console.error('[SELFTEST] Register error:', {
          status: errorStatus,
          message: errorMessage,
          data: errorData,
        });

        // Construire un message d'erreur détaillé
        let errorDetails = errorMessage;
        if (errorStatus === 422) {
          // Erreur de validation
          const validationErrors = errorData?.detail || errorData;
          if (typeof validationErrors === 'string') {
            errorDetails = `422 Validation Error: ${validationErrors}`;
          } else if (Array.isArray(validationErrors)) {
            errorDetails = `422 Validation Errors:\n${validationErrors.map((e: any) => 
              `- ${e.loc?.join('.')}: ${e.msg}`
            ).join('\n')}`;
          } else if (typeof validationErrors === 'object') {
            errorDetails = `422 Validation Error: ${JSON.stringify(validationErrors, null, 2)}`;
          }
        } else if (errorStatus) {
          errorDetails = `${errorStatus} ${errorMessage}`;
          if (errorData?.detail) {
            errorDetails += `\n${JSON.stringify(errorData.detail, null, 2)}`;
          }
        }

        updateResult('Register', 'error', errorDetails);
      }

      // Test 3: Login
      updateResult('Login', 'running', `Logging in as ${testEmail}...`);
      try {
        // Logger le payload (sans password)
        console.log('[SELFTEST] Login payload:', { username: testEmail, password: '***' });
        console.log('[SELFTEST] Login endpoint: POST /api/auth/login (form-urlencoded)');

        const loginResponse = await auth.login(testEmail, testPassword);
        
        if (loginResponse.access_token) {
          setToken(loginResponse.access_token);
          updateResult('Login', 'success', `Token: ${loginResponse.access_token.substring(0, 30)}...`);
          
          // Test 4: Get Me
          updateResult('Get Me', 'running', 'Fetching user info...');
          try {
            const userResponse = await auth.getMe();
            
            if (userResponse.email === testEmail) {
              updateResult('Get Me', 'success', `User: ${userResponse.email} (ID: ${userResponse.id})`);
            } else {
              updateResult('Get Me', 'error', `Email mismatch: ${userResponse.email}`);
            }
          } catch (error: any) {
            const errorStatus = error.response?.status;
            const errorData = error.response?.data;
            const errorDetails = errorStatus 
              ? `${errorStatus} ${error.message || 'Failed'}` 
              : (error.message || 'Failed');
            if (errorData?.detail) {
              updateResult('Get Me', 'error', `${errorDetails}\n${JSON.stringify(errorData.detail, null, 2)}`);
            } else {
              updateResult('Get Me', 'error', errorDetails);
            }
          }
        } else {
          updateResult('Login', 'error', 'No token received');
        }
      } catch (error: any) {
        // Logger les détails de l'erreur
        const errorStatus = error.response?.status;
        const errorData = error.response?.data;
        const errorMessage = error.message || 'Failed';
        
        console.error('[SELFTEST] Login error:', {
          status: errorStatus,
          message: errorMessage,
          data: errorData,
        });

        // Construire un message d'erreur détaillé
        let errorDetails = errorMessage;
        if (errorStatus === 401) {
          errorDetails = `401 Unauthorized: ${errorData?.detail || errorMessage}`;
        } else if (errorStatus) {
          errorDetails = `${errorStatus} ${errorMessage}`;
          if (errorData?.detail) {
            errorDetails += `\n${JSON.stringify(errorData.detail, null, 2)}`;
          }
        }

        updateResult('Login', 'error', errorDetails);
      }

    } catch (error: any) {
      console.error('Test error:', error);
    } finally {
      setRunning(false);
    }
  };

  const getStatusIcon = (status: TestResult['status']) => {
    switch (status) {
      case 'pending': return '⏳';
      case 'running': return '🔄';
      case 'success': return '✅';
      case 'error': return '❌';
    }
  };

  const successCount = results.filter(r => r.status === 'success').length;
  const errorCount = results.filter(r => r.status === 'error').length;

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <View style={styles.content}>
          <Text style={styles.title}>🧪 Auth Self-Test</Text>
          
          <View style={styles.infoCard}>
            <Text style={styles.infoLabel}>API URL:</Text>
            <Text style={styles.infoValue}>{getApiUrl()}</Text>
          </View>

          {token && (
            <View style={styles.infoCard}>
              <Text style={styles.infoLabel}>Token (truncated):</Text>
              <Text style={styles.infoValue}>{token.substring(0, 40)}...</Text>
            </View>
          )}

          <TouchableOpacity
            style={[styles.button, running && styles.buttonDisabled]}
            onPress={runTests}
            disabled={running}
          >
            {running ? (
              <ActivityIndicator color={colors.text} />
            ) : (
              <Text style={styles.buttonText}>Run Auth E2E</Text>
            )}
          </TouchableOpacity>

          {results.length > 0 && (
            <>
              <View style={styles.summary}>
                <Text style={styles.summaryText}>
                  ✅ {successCount} passed  ❌ {errorCount} failed
                </Text>
              </View>

              <View style={styles.resultsContainer}>
                {results.map((result, index) => (
                  <View key={index} style={styles.resultCard}>
                    <View style={styles.resultHeader}>
                      <Text style={styles.resultIcon}>{getStatusIcon(result.status)}</Text>
                      <Text style={styles.resultStep}>{result.step}</Text>
                    </View>
                    <Text style={styles.resultDetails}>{result.details}</Text>
                  </View>
                ))}
              </View>
            </>
          )}
        </View>
      </ScrollView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollView: {
    flex: 1,
  },
  content: {
    padding: spacing.xl,
  },
  title: {
    fontSize: fonts.sizes.xxl,
    fontWeight: '700',
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.xl,
  },
  infoCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.md,
  },
  infoLabel: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    marginBottom: spacing.xs,
  },
  infoValue: {
    fontSize: fonts.sizes.sm,
    color: colors.text,
    fontFamily: 'monospace',
  },
  button: {
    backgroundColor: colors.accent,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    alignItems: 'center',
    marginVertical: spacing.lg,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonText: {
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: '600',
  },
  summary: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.lg,
  },
  summaryText: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    textAlign: 'center',
    fontWeight: '600',
  },
  resultsContainer: {
    gap: spacing.md,
  },
  resultCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
  },
  resultHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.xs,
  },
  resultIcon: {
    fontSize: 20,
    marginRight: spacing.sm,
  },
  resultStep: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    fontWeight: '600',
  },
  resultDetails: {
    fontSize: fonts.sizes.sm,
    color: colors.textMuted,
    fontFamily: 'monospace',
    marginLeft: 28,
  },
});

