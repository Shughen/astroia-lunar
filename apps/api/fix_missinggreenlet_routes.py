#!/usr/bin/env python3
"""
Script pour fixer systématiquement le pattern MissingGreenlet dans les routes.
Remplace tous les accès à current_user.<attr> par extraction de primitives au début.
"""

import re
from pathlib import Path

def fix_natal_py():
    """Fix routes/natal.py"""
    file_path = Path("routes/natal.py")
    content = file_path.read_text()

    # Pattern 1: Ajouter extraction de primitives au début de calculate_natal_chart
    old_pattern = r'''(@router\.post\("/natal-chart"\)
async def calculate_natal_chart\(
    data: NatalChartRequest,
    current_user: User = Depends\(get_current_user\),
    db: AsyncSession = Depends\(get_db\)
\):
    """.*?"""
    # Fallback birth_time)'''

    new_code = r'''@router.post("/natal-chart")
async def calculate_natal_chart(
    data: NatalChartRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Calcule le thème natal et le sauvegarde
    IDEMPOTENT: Si un thème existe déjà avec les mêmes paramètres, retourne l'existant sans recalculer
    """

    # 🔒 CRITIQUE: Extraire primitives IMMÉDIATEMENT pour éviter MissingGreenlet
    user_id = int(current_user.id)
    user_email = str(current_user.email) if hasattr(current_user, 'email') and current_user.email else f"dev+{user_id}@local.dev"
    birth_date_existing = str(current_user.birth_date) if hasattr(current_user, 'birth_date') and current_user.birth_date else None
    birth_time_existing = str(current_user.birth_time) if hasattr(current_user, 'birth_time') and current_user.birth_time else None
    birth_latitude_existing = current_user.birth_latitude if hasattr(current_user, 'birth_latitude') else None
    birth_longitude_existing = current_user.birth_longitude if hasattr(current_user, 'birth_longitude') else None
    birth_timezone_existing = str(current_user.birth_timezone) if hasattr(current_user, 'birth_timezone') and current_user.birth_timezone else None

    # Fallback birth_time'''

    content = re.sub(old_pattern, new_code, content, flags=re.DOTALL)

    # Pattern 2: Remplacer current_user.id par user_id
    content = re.sub(r'\bcurrent_user\.id\b', 'user_id', content)

    # Pattern 3: Remplacer current_user.email par user_email
    content = re.sub(r'getattr\(current_user, "email", f"dev\+\{current_user\.id\}@local\.dev"\)', 'user_email', content)

    # Pattern 4: Remplacer current_user.birth_date par birth_date_existing
    content = re.sub(r'\bcurrent_user\.birth_date\b', 'birth_date_existing', content)

    # Pattern 5: Remplacer current_user.birth_time par birth_time_existing
    content = re.sub(r'\bcurrent_user\.birth_time\b', 'birth_time_existing', content)

    # Pattern 6: Remplacer current_user.birth_latitude par birth_latitude_existing
    content = re.sub(r'\bcurrent_user\.birth_latitude\b', 'birth_latitude_existing', content)

    # Pattern 7: Remplacer current_user.birth_longitude par birth_longitude_existing
    content = re.sub(r'\bcurrent_user\.birth_longitude\b', 'birth_longitude_existing', content)

    # Pattern 8: Remplacer current_user.birth_timezone par birth_timezone_existing
    content = re.sub(r'\bcurrent_user\.birth_timezone\b', 'birth_timezone_existing', content)

    # Pattern 9: Remplacer current_user.birth_place_name par birth_place_name_existing
    content = re.sub(r'\bcurrent_user\.birth_place_name\b', 'birth_place_name_existing', content)

    # Pattern 10: Remplacer getattr(current_user, 'birth_timezone', None)
    content = re.sub(r"getattr\(current_user, 'birth_timezone', None\)", 'birth_timezone_existing', content)

    file_path.write_text(content)
    print(f"✅ {file_path} fixed")

def fix_natal_interpretation_py():
    """Fix routes/natal_interpretation.py"""
    file_path = Path("routes/natal_interpretation.py")
    if not file_path.exists():
        print(f"⏭️  {file_path} not found, skipping")
        return

    content = file_path.read_text()

    # Ajouter extraction au début de chaque endpoint qui utilise current_user
    # Chercher @router.get et ajouter extraction après la docstring

    # Remplacer tous les current_user.id par user_id
    content = re.sub(r'\bcurrent_user\.id\b', 'user_id', content)

    # Chercher tous les endpoints et ajouter extraction
    lines = content.split('\n')
    new_lines = []
    in_function = False
    added_extraction = False

    for i, line in enumerate(lines):
        new_lines.append(line)

        # Détecter début de fonction
        if line.strip().startswith('@router.'):
            in_function = True
            added_extraction = False

        # Ajouter extraction après docstring si on trouve current_user
        if in_function and not added_extraction:
            if '"""' in line or "'''" in line:
                # On est à la fin de la docstring
                # Vérifier si les prochaines lignes utilisent current_user
                next_50_lines = '\n'.join(lines[i:min(i+50, len(lines))])
                if 'current_user' in next_50_lines:
                    new_lines.append('')
                    new_lines.append('    # 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet')
                    new_lines.append('    user_id = int(current_user.id)')
                    added_extraction = True

            # Désactiver après quelques lignes
            if i > 10:
                in_function = False

    content = '\n'.join(new_lines)
    file_path.write_text(content)
    print(f"✅ {file_path} fixed")

def fix_lunar_py():
    """Fix routes/lunar.py"""
    file_path = Path("routes/lunar.py")
    if not file_path.exists():
        print(f"⏭️  {file_path} not found, skipping")
        return

    content = file_path.read_text()

    # Remplacer tous les current_user.id par user_id
    content = re.sub(r'\bcurrent_user\.id\b', 'user_id', content)

    # Ajouter extraction au début de chaque endpoint
    lines = content.split('\n')
    new_lines = []
    in_function = False
    added_extraction = False

    for i, line in enumerate(lines):
        new_lines.append(line)

        # Détecter début de fonction
        if line.strip().startswith('@router.'):
            in_function = True
            added_extraction = False

        # Ajouter extraction après docstring
        if in_function and not added_extraction:
            if '"""' in line or "'''" in line:
                next_50_lines = '\n'.join(lines[i:min(i+50, len(lines))])
                if 'current_user' in next_50_lines:
                    new_lines.append('')
                    new_lines.append('    # 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet')
                    new_lines.append('    user_id = int(current_user.id)')
                    added_extraction = True

            if i > 10:
                in_function = False

    content = '\n'.join(new_lines)
    file_path.write_text(content)
    print(f"✅ {file_path} fixed")

if __name__ == "__main__":
    print("🔧 Fixing MissingGreenlet pattern in routes...")
    fix_natal_py()
    fix_natal_interpretation_py()
    fix_lunar_py()
    print("\n✅ All files fixed!")
