-- ===========================================
-- Astroia Lunar - Seed Demo User
-- ===========================================
-- Crée un utilisateur de démo pour tester l'API
-- ===========================================

-- Supprimer l'utilisateur démo s'il existe déjà
DELETE FROM public.users WHERE email = 'demo@astroia.com';

-- Créer l'utilisateur démo
-- Note: Le mot de passe hashé correspond à "DemoPass123!"
-- Vous devrez le générer via l'API /api/auth/register ou avec passlib
INSERT INTO public.users (
    email,
    hashed_password,
    birth_date,
    birth_time,
    birth_latitude,
    birth_longitude,
    birth_place_name,
    birth_timezone,
    is_active,
    is_premium,
    created_at
) VALUES (
    'demo@astroia.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWU6O2CO',  -- DemoPass123!
    '1989-04-15',
    '17:55',
    '48.8566',
    '2.3522',
    'Paris, France',
    'Europe/Paris',
    true,
    false,
    NOW()
);

-- Vérifier la création
SELECT 
    id,
    email,
    birth_place_name,
    is_active,
    created_at
FROM public.users 
WHERE email = 'demo@astroia.com';

-- Afficher le message de succès
SELECT '✅ Utilisateur démo créé avec succès!' as status;
SELECT '📧 Email: demo@astroia.com' as info;
SELECT '🔑 Password: DemoPass123!' as credentials;
