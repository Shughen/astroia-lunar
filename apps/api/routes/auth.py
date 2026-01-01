"""Routes d'authentification"""

from fastapi import APIRouter, Depends, HTTPException, status, Request, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional, Tuple
from uuid import UUID
import logging

from database import get_db
from models.user import User
from config import settings

logger = logging.getLogger(__name__)

router = APIRouter()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)


# === SCHEMAS ===
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    birth_date: Optional[str] = None
    birth_time: Optional[str] = None
    birth_latitude: Optional[float] = None
    birth_longitude: Optional[float] = None
    birth_place_name: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    email: str
    birth_date: Optional[str]
    birth_time: Optional[str]
    birth_place_name: Optional[str]
    is_premium: bool
    created_at: datetime


# === HELPERS ===
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # python-jose requires "sub" to be a string
    if "sub" in to_encode and isinstance(to_encode["sub"], int):
        to_encode["sub"] = str(to_encode["sub"])
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


async def resolve_dev_user(
    user_identifier: str,
    db: AsyncSession
) -> Tuple[User, str]:
    """
    Résolution déterministe d'un utilisateur en mode DEV_AUTH_BYPASS.

    Args:
        user_identifier: UUID string, integer string, ou email
        db: Session de base de données

    Returns:
        Tuple (User, method) où method décrit comment l'utilisateur a été résolu

    Raises:
        HTTPException: Si l'utilisateur ne peut pas être résolu
    """
    # Tentative 1: Traiter comme UUID et chercher par dev_external_id
    try:
        user_uuid = UUID(user_identifier)
        result = await db.execute(
            select(User).where(User.dev_external_id == str(user_uuid))
        )
        user = result.scalar_one_or_none()

        if user:
            logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé via dev_external_id={user_uuid}")
            return user, "header_uuid"

        # Créer un nouvel utilisateur dev avec cet UUID
        logger.info(f"🆕 DEV_AUTH_BYPASS: création user avec dev_external_id={user_uuid}")
        try:
            # Utiliser un hash pré-calculé pour éviter les problèmes avec bcrypt
            # Hash de "dev-password" pré-calculé avec bcrypt (généré avec bcrypt.gensalt())
            dev_password_hash = "$2b$12$A2rj/gsY/fAzI5GY9TCQFOByzS/J8TIL3ElOyFSAAxHzVdg.OluOq"
            
            new_user = User(
                email=f"dev+{str(user_uuid)[:8]}@local.dev",
                hashed_password=dev_password_hash,
                dev_external_id=str(user_uuid),
                is_active=True,
                is_premium=False
            )
            db.add(new_user)
            await db.commit()
            await db.refresh(new_user)
            logger.info(f"✅ DEV_AUTH_BYPASS: user créé - id={new_user.id}, email={new_user.email}")
            return new_user, "header_uuid_created"
        except IntegrityError as e:
            # L'utilisateur existe peut-être déjà (email ou dev_external_id en double)
            await db.rollback()
            logger.warning(f"⚠️ DEV_AUTH_BYPASS: échec création user avec dev_external_id={user_uuid}, erreur: {e}")
            # Réessayer de chercher par dev_external_id (peut-être créé entre temps)
            result = await db.execute(
                select(User).where(User.dev_external_id == str(user_uuid))
            )
            user = result.scalar_one_or_none()
            if user:
                logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé après rollback via dev_external_id={user_uuid}")
                return user, "header_uuid"
            # Si toujours pas trouvé, essayer par email généré
            email = f"dev+{str(user_uuid)[:8]}@local.dev"
            result = await db.execute(select(User).where(User.email == email))
            user = result.scalar_one_or_none()
            if user:
                logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé via email={email} après échec création")
                return user, "header_uuid_email_fallback"
            # Si toujours pas trouvé, continuer vers les autres méthodes de résolution

    except (ValueError, TypeError):
        # Pas un UUID valide, continuer
        pass

    # Tentative 2: Traiter comme integer ID
    try:
        user_id = int(user_identifier)
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if user:
            logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé via id={user_id}")
            return user, "header_int"

        logger.warning(f"⚠️ DEV_AUTH_BYPASS: user_id={user_id} introuvable")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"DEV_AUTH_BYPASS: user avec id={user_id} introuvable"
        )
    except (ValueError, TypeError):
        # Pas un integer valide
        pass

    # Tentative 3: Traiter comme email
    result = await db.execute(select(User).where(User.email == user_identifier))
    user = result.scalar_one_or_none()

    if user:
        logger.info(f"✅ DEV_AUTH_BYPASS: user trouvé via email={user_identifier}")
        return user, "header_email"

    # Tentative 4: Fallback vers dev@local.dev (utilisateur par défaut pour DEV)
    logger.info("📥 DEV_AUTH_BYPASS: pas de header/env, fallback vers dev@local.dev")
    result = await db.execute(select(User).where(User.email == "dev@local.dev"))
    dev_user = result.scalar_one_or_none()

    if dev_user:
        logger.info(f"✅ DEV_AUTH_BYPASS resolved: user_id={dev_user.id}, method=dev_default")
        return dev_user, "dev_default"

    # Créer le user dev@local.dev si il n'existe pas
    logger.info("🆕 DEV_AUTH_BYPASS: création user dev@local.dev")
    try:
        # Utiliser un hash pré-calculé pour éviter les problèmes avec bcrypt
        # Hash de "dev-password" pré-calculé avec bcrypt (généré avec bcrypt.gensalt())
        dev_password_hash = "$2b$12$A2rj/gsY/fAzI5GY9TCQFOByzS/J8TIL3ElOyFSAAxHzVdg.OluOq"
        
        new_dev_user = User(
            email="dev@local.dev",
            hashed_password=dev_password_hash,
            is_active=True,
            is_premium=False
        )
        db.add(new_dev_user)
        await db.commit()
        await db.refresh(new_dev_user)
        logger.info(f"✅ DEV_AUTH_BYPASS: user dev@local.dev créé - id={new_dev_user.id}")
        return new_dev_user, "dev_default_created"
    except IntegrityError:
        # L'utilisateur a peut-être été créé entre temps
        await db.rollback()
        result = await db.execute(select(User).where(User.email == "dev@local.dev"))
        dev_user = result.scalar_one_or_none()
        if dev_user:
            logger.info(f"✅ DEV_AUTH_BYPASS: user dev@local.dev trouvé après rollback - id={dev_user.id}")
            return dev_user, "dev_default"
    except Exception as e:
        # Autres erreurs (comme bcrypt)
        await db.rollback()
        logger.warning(f"⚠️ DEV_AUTH_BYPASS: erreur lors de la création de dev@local.dev: {e}")
        # Réessayer de chercher l'utilisateur
        result = await db.execute(select(User).where(User.email == "dev@local.dev"))
        dev_user = result.scalar_one_or_none()
        if dev_user:
            logger.info(f"✅ DEV_AUTH_BYPASS: user dev@local.dev trouvé après erreur - id={dev_user.id}")
            return dev_user, "dev_default"

    # Échec: aucune résolution possible (ne devrait jamais arriver si dev@local.dev fonctionne)
    logger.error(f"❌ DEV_AUTH_BYPASS: impossible de résoudre user avec identifier={user_identifier}")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"DEV_AUTH_BYPASS: impossible de résoudre user avec identifier={user_identifier}"
    )


async def get_current_user(
    x_dev_user_id: Optional[str] = Header(default=None, alias="X-Dev-User-Id"),
    token: Optional[str] = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    """Dependency pour récupérer le user connecté"""
    from jose.exceptions import ExpiredSignatureError

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Impossible de valider les identifiants",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # ===== MODE DEV: bypass avec header X-Dev-User-Id (uniquement en development) =====
    if settings.APP_ENV == "development" and settings.DEV_AUTH_BYPASS:
        logger.info("🔧 DEV_AUTH_BYPASS enabled")

        # Ordre de résolution:
        # 1. Header X-Dev-User-Id
        # 2. ENV variable DEV_USER_ID
        # 3. User explicite dev@local.dev (créé si nécessaire)

        user_identifier = None

        if x_dev_user_id:
            user_identifier = x_dev_user_id
            logger.info(f"📥 DEV_AUTH_BYPASS: X-Dev-User-Id header={user_identifier}")
        elif settings.DEV_USER_ID:
            user_identifier = settings.DEV_USER_ID
            logger.info(f"📥 DEV_AUTH_BYPASS: DEV_USER_ID env={user_identifier}")
        else:
            # Fallback: chercher ou créer user avec email dev@local.dev
            logger.info("📥 DEV_AUTH_BYPASS: pas de header/env, fallback vers dev@local.dev")
            result = await db.execute(select(User).where(User.email == "dev@local.dev"))
            dev_user = result.scalar_one_or_none()

            if dev_user:
                logger.info(f"✅ DEV_AUTH_BYPASS resolved: user_id={dev_user.id}, method=dev_default")
                return dev_user

            # Créer le user dev@local.dev
            logger.info("🆕 DEV_AUTH_BYPASS: création user dev@local.dev")
            try:
                # Utiliser un hash pré-calculé pour éviter les problèmes avec bcrypt
                # Hash de "dev-password" pré-calculé avec bcrypt (généré avec bcrypt.gensalt())
                dev_password_hash = "$2b$12$A2rj/gsY/fAzI5GY9TCQFOByzS/J8TIL3ElOyFSAAxHzVdg.OluOq"
                dev_user = User(
                    email="dev@local.dev",
                    hashed_password=dev_password_hash,
                    is_active=True,
                    is_premium=False
                )
                db.add(dev_user)
                await db.commit()
                await db.refresh(dev_user)
                logger.info(f"✅ DEV_AUTH_BYPASS created: user_id={dev_user.id}, method=dev_default")
                return dev_user
            except IntegrityError:
                # L'utilisateur a peut-être été créé entre temps
                await db.rollback()
                result = await db.execute(select(User).where(User.email == "dev@local.dev"))
                dev_user = result.scalar_one_or_none()
                if dev_user:
                    logger.info(f"✅ DEV_AUTH_BYPASS: user dev@local.dev trouvé après rollback - id={dev_user.id}")
                    return dev_user
                raise

        # Si on a un user_identifier, résoudre via resolve_dev_user()
        if user_identifier:
            user, method = await resolve_dev_user(user_identifier, db)
            logger.info(f"✅ DEV_AUTH_BYPASS resolved: user_id={user.id}, method={method}")
            return user

    # ===== MODE NORMAL: JWT =====
    if not token:
        logger.warning("❌ JWT: token manquant dans header Authorization")
        raise credentials_exception

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id_str: str = payload.get("sub")
        if user_id_str is None:
            logger.warning("❌ JWT decode: 'sub' claim manquant")
            raise credentials_exception
        # Convert string sub to int
        try:
            user_id: int = int(user_id_str)
        except (ValueError, TypeError):
            logger.warning(f"❌ JWT decode: 'sub' n'est pas un entier valide: {user_id_str}")
            raise credentials_exception
    except ExpiredSignatureError:
        logger.warning("❌ JWT decode: token expiré")
        raise credentials_exception
    except JWTError as e:
        logger.warning(f"❌ JWT decode: erreur de signature/format: {e}")
        raise credentials_exception

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if user is None:
        logger.warning(f"❌ User non trouvé en DB: user_id={user_id}")
        raise credentials_exception

    return user


# === ROUTES ===
@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: AsyncSession = Depends(get_db)):
    """Inscription d'un nouvel utilisateur"""
    
    # Vérifier si l'email existe déjà
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cet email est déjà utilisé"
        )
    
    # Créer l'utilisateur
    user = User(
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        birth_date=user_data.birth_date,
        birth_time=user_data.birth_time,
        birth_latitude=str(user_data.birth_latitude) if user_data.birth_latitude else None,
        birth_longitude=str(user_data.birth_longitude) if user_data.birth_longitude else None,
        birth_place_name=user_data.birth_place_name
    )
    
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    # Générer le token
    access_token = create_access_token(data={"sub": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """Connexion"""
    
    # Trouver l'utilisateur
    result = await db.execute(select(User).where(User.email == form_data.username))
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Générer le token
    access_token = create_access_token(data={"sub": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Récupère le profil de l'utilisateur connecté"""
    return current_user

