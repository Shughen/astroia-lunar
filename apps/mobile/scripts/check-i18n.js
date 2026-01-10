#!/usr/bin/env node
/**
 * i18n Key Parity Checker
 *
 * Validates that FR and EN translation files have matching keys.
 * Exits with code 1 if mismatches found, 0 otherwise.
 */

const fs = require('fs');
const path = require('path');

// Paths to translation files
const FR_PATH = path.join(__dirname, '../i18n/fr.json');
const EN_PATH = path.join(__dirname, '../i18n/en.json');

/**
 * Flatten nested JSON to dot notation
 * Example: { a: { b: "val" } } => { "a.b": "val" }
 */
function flattenKeys(obj, prefix = '') {
  const keys = [];

  for (const key in obj) {
    const fullKey = prefix ? `${prefix}.${key}` : key;

    if (typeof obj[key] === 'object' && !Array.isArray(obj[key]) && obj[key] !== null) {
      keys.push(...flattenKeys(obj[key], fullKey));
    } else {
      keys.push(fullKey);
    }
  }

  return keys;
}

/**
 * Main validation logic
 */
function checkI18nParity() {
  console.log('🔍 Checking i18n key parity...\n');

  // Load translation files
  let frData, enData;

  try {
    frData = JSON.parse(fs.readFileSync(FR_PATH, 'utf8'));
    enData = JSON.parse(fs.readFileSync(EN_PATH, 'utf8'));
  } catch (error) {
    console.error('❌ Error reading translation files:', error.message);
    process.exit(1);
  }

  // Flatten keys
  const frKeys = flattenKeys(frData).sort();
  const enKeys = flattenKeys(enData).sort();

  // Find differences
  const missingInEn = frKeys.filter(key => !enKeys.includes(key));
  const extraInEn = enKeys.filter(key => !frKeys.includes(key));

  // Report results
  console.log(`📊 Statistics:`);
  console.log(`   FR keys: ${frKeys.length}`);
  console.log(`   EN keys: ${enKeys.length}\n`);

  let hasErrors = false;

  if (missingInEn.length > 0) {
    hasErrors = true;
    console.log(`❌ Missing in EN (${missingInEn.length} keys):`);
    missingInEn.forEach(key => console.log(`   - ${key}`));
    console.log('');
  }

  if (extraInEn.length > 0) {
    hasErrors = true;
    console.log(`⚠️  Extra in EN (${extraInEn.length} keys):`);
    extraInEn.forEach(key => console.log(`   - ${key}`));
    console.log('');
  }

  if (!hasErrors) {
    console.log('✅ i18n key parity check passed!');
    console.log('   All keys match between FR and EN.\n');
    process.exit(0);
  } else {
    console.log('💡 Action required:');
    console.log('   - Add missing EN translations');
    console.log('   - Remove extra EN keys');
    console.log('   - Run: npm run check:i18n\n');
    process.exit(1);
  }
}

// Run check
checkI18nParity();
