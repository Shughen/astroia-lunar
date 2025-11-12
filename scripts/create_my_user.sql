-- ===========================================
-- Astroia Lunar - Créer Mon Utilisateur
-- ===========================================
-- Email: remi.beaurain@gmail.com
-- Password: 123456
-- ===========================================

-- Supprimer l'utilisateur s'il existe déjà
DELETE FROM public.users WHERE email = 'remi.beaurain@gmail.com';

-- Créer l'utilisateur
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
    'remi.beaurain@gmail.com',
    '$2b$12$/PEPHGvPTM3UUMrAf9X8MOQOqax47lWmkBfu4qRsOo8kgGPjY6u7a',  -- Hash de "123456"
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
    birth_date,
    birth_time,
    birth_place_name,
    is_active,
    is_premium,
    created_at
FROM public.users 
WHERE email = 'remi.beaurain@gmail.com';

-- Message de succès
SELECT '✅ Utilisateur créé avec succès!' as status;
SELECT '📧 Email: remi.beaurain@gmail.com' as info;
SELECT '🔑 Password: 123456' as credentials;

