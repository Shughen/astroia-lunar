/**
 * Mini analytics layer (console-based pour MVP)
 * À remplacer par Firebase Analytics / Posthog / etc. en production
 */

export type AnalyticsEvent =
  | { name: 'daily_climate_view'; properties: { firstOfDay: boolean; source: 'home' | 'lunar' } }
  | { name: 'daily_climate_reset_dev'; properties: { timestamp: number } };

export function trackEvent(event: AnalyticsEvent): void {
  if (__DEV__) {
    console.log(`[Analytics] ${event.name}`, event.properties);
  }
  // TODO: Intégrer analytics externe (Firebase, Posthog, etc.)
}
