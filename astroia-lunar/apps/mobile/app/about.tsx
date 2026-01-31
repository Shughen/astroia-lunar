/**
 * Page À propos / FAQ
 *
 * Contient des informations sur le fonctionnement de l'app
 * et une FAQ avec mention discrète de l'IA.
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Linking,
} from 'react-native';
import { router } from 'expo-router';

export default function AboutScreen() {
  return (
    <ScrollView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity
          style={styles.backButton}
          onPress={() => router.back()}
          hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
        >
          <Text style={styles.backButtonText}>← Retour</Text>
        </TouchableOpacity>

        <Text style={styles.title}>À propos de Lunation</Text>
      </View>

      {/* Comment ça marche */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>🌙 Comment ça marche ?</Text>
        <Text style={styles.paragraph}>
          Lunation calcule tes cycles lunaires personnels en fonction de ta date, heure et lieu de naissance.
        </Text>
        <Text style={styles.paragraph}>
          Chaque mois, la Lune revient à sa position natale : c'est ta révolution lunaire personnelle.
          Ce moment marque le début d'un nouveau cycle émotionnel et intuitif.
        </Text>
        <Text style={styles.paragraph}>
          L'application te guide à travers les différentes phases de la Lune et leurs influences sur ton quotidien.
        </Text>
      </View>

      {/* FAQ */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>❓ FAQ</Text>

        {/* Question 1 */}
        <View style={styles.faqItem}>
          <Text style={styles.question}>
            Comment sont générées les interprétations ?
          </Text>
          <Text style={styles.answer}>
            Les interprétations sont générées par intelligence artificielle et personnalisées selon ton profil astrologique unique.
          </Text>
        </View>

        {/* Question 2 */}
        <View style={styles.faqItem}>
          <Text style={styles.question}>
            Mes données sont-elles protégées ?
          </Text>
          <Text style={styles.answer}>
            Oui, tes données personnelles sont stockées de manière sécurisée.
            Nous ne partageons jamais tes informations avec des tiers.
          </Text>
          <TouchableOpacity
            onPress={() => Linking.openURL('https://lunation.app/privacy')}
          >
            <Text style={styles.link}>Voir la politique de confidentialité →</Text>
          </TouchableOpacity>
        </View>

        {/* Question 3 */}
        <View style={styles.faqItem}>
          <Text style={styles.question}>
            Qu'est-ce que la Lune Void of Course (VoC) ?
          </Text>
          <Text style={styles.answer}>
            La période "Void of Course" correspond au moment où la Lune n'effectue plus d'aspect majeur
            avant de changer de signe. C'est un temps propice à l'introspection plutôt qu'aux nouvelles initiatives.
          </Text>
        </View>

        {/* Question 4 */}
        <View style={styles.faqItem}>
          <Text style={styles.question}>
            Comment fonctionne le journal ?
          </Text>
          <Text style={styles.answer}>
            Le journal te permet de noter tes ressentis et observations au fil des phases lunaires.
            Tu peux créer plusieurs entrées par jour et les retrouver dans l'historique.
          </Text>
        </View>
      </View>

      {/* Footer */}
      <View style={styles.footer}>
        <Text style={styles.footerText}>Lunation v3.0</Text>
        <Text style={styles.footerText}>Fait avec 🌙 pour les curieux du ciel</Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0A0E27',
  },
  header: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#1A1F3E',
    borderBottomWidth: 2,
    borderBottomColor: '#8B7BF7',
    position: 'relative',
  },
  backButton: {
    position: 'absolute',
    top: 60,
    left: 20,
    zIndex: 10,
    padding: 8,
    marginLeft: -8,
    marginTop: -8,
  },
  backButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FFFFFF',
    textAlign: 'center',
    marginTop: 24,
  },
  section: {
    margin: 16,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#8B7BF7',
    marginBottom: 16,
  },
  paragraph: {
    fontSize: 15,
    color: '#FFFFFF',
    lineHeight: 22,
    marginBottom: 12,
  },
  faqItem: {
    marginBottom: 20,
    paddingBottom: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#2D3561',
  },
  question: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
    marginBottom: 8,
  },
  answer: {
    fontSize: 14,
    color: '#A0A0B0',
    lineHeight: 20,
  },
  link: {
    fontSize: 14,
    color: '#8B7BF7',
    marginTop: 8,
    fontWeight: '500',
  },
  footer: {
    padding: 20,
    alignItems: 'center',
    marginBottom: 40,
  },
  footerText: {
    fontSize: 12,
    color: '#A0A0B0',
    marginBottom: 4,
  },
});
