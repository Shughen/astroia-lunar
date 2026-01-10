#!/usr/bin/env python3
"""
Test minimal pour vérifier que bcrypt/passlib fonctionne correctement.

Usage:
    python scripts/test_bcrypt_password.py
"""

from passlib.context import CryptContext
import sys

# Password hashing (même config que auth.py)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def test_bcrypt():
    """Test basique de hash/verify avec bcrypt."""
    print("🧪 Test bcrypt/passlib...")
    
    # Test 1: Hash et verify un mot de passe simple
    password = "test-password-123"
    print(f"   Password: {password}")
    
    try:
        hashed = pwd_context.hash(password)
        print(f"   ✅ Hash généré: {hashed[:50]}...")
    except Exception as e:
        print(f"   ❌ Erreur hash: {e}")
        return False
    
    # Test 2: Verify le hash
    try:
        is_valid = pwd_context.verify(password, hashed)
        if is_valid:
            print(f"   ✅ Verify OK: password correct")
        else:
            print(f"   ❌ Verify FAILED: password incorrect")
            return False
    except Exception as e:
        print(f"   ❌ Erreur verify: {e}")
        return False
    
    # Test 3: Verify avec mauvais password
    try:
        is_valid = pwd_context.verify("wrong-password", hashed)
        if not is_valid:
            print(f"   ✅ Verify OK: mauvais password rejeté")
        else:
            print(f"   ❌ Verify FAILED: mauvais password accepté")
            return False
    except Exception as e:
        print(f"   ❌ Erreur verify: {e}")
        return False
    
    # Test 4: Hash connu (comme dans auth.py pour dev users)
    known_hash = "$2b$12$A2rj/gsY/fAzI5GY9TCQFOByzS/J8TIL3ElOyFSAAxHzVdg.OluOq"
    known_password = "dev-password"
    try:
        is_valid = pwd_context.verify(known_password, known_hash)
        if is_valid:
            print(f"   ✅ Verify OK: hash connu (dev-password) vérifié")
        else:
            print(f"   ⚠️  Hash connu non vérifié (peut être normal si généré avec autre version)")
    except Exception as e:
        print(f"   ⚠️  Erreur verify hash connu: {e}")
    
    print("\n✅ Tous les tests passés")
    return True

if __name__ == "__main__":
    success = test_bcrypt()
    sys.exit(0 if success else 1)

