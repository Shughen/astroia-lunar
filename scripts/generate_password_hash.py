#!/usr/bin/env python3
"""
Script pour générer un hash bcrypt pour un mot de passe
Utile pour créer des utilisateurs manuellement en SQL
"""
import sys
import bcrypt


def generate_hash(password: str) -> str:
    """Génère un hash bcrypt pour un mot de passe"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("🔑 Entrez le mot de passe à hasher: ")
    
    hashed = generate_hash(password)
    
    print("\n✅ Hash généré avec succès!")
    print(f"📝 Mot de passe: {password}")
    print(f"🔒 Hash bcrypt:")
    print(f"   {hashed}")
    print("\n💡 Utilisez ce hash dans votre INSERT SQL:")
    print(f"   hashed_password = '{hashed}'")

