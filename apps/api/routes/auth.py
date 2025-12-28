"""Routes d'authentification"""

from fastapi import APIRouter, Depends, HTTPException, status, Request, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
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
    
    # Mode DEV: bypass avec header X-Dev-User-Id (uniquement en development)
    # Vérifier le bypass AVANT de vérifier le token JWT
    if settings.APP_ENV == "development" and settings.DEV_AUTH_BYPASS:
        logger.info("🔧 DEV_AUTH_BYPASS activé")
        
        if x_dev_user_id:
            logger.info(f"📥 Header X-Dev-User-Id reçu: {x_dev_user_id}")
            try:
                # Traiter X-Dev-User-Id comme UUID (string) pour validation
                user_id_uuid = UUID(x_dev_user_id)
                logger.info(f"✅ DEV_AUTH_BYPASS: UUID valide reçu - {user_id_uuid}")
                
                # Pour DEV_AUTH_BYPASS, on cherche ou crée un utilisateur de dev dans la DB
                # car les routes (comme lunar_returns) ont besoin de user.id (Integer) pour fonctionner
                # On cherche d'abord le premier utilisateur dans la DB
                result = await db.execute(select(User).limit(1))
                dev_user = result.scalar_one_or_none()
                
                if dev_user:
                    logger.info(f"✅ DEV_AUTH_BYPASS: utilisation user existant - id={dev_user.id}, email={dev_user.email}")
                    return dev_user
                else:
                    # Si aucun utilisateur dans la DB, créer un utilisateur de dev
                    logger.warning("⚠️ DEV_AUTH_BYPASS: aucun utilisateur trouvé, création d'un utilisateur de dev")
                    dev_user = User(
                        email=f"dev-user-{str(user_id_uuid)[:8]}@dev.local",
                        hashed_password=hash_password("dev-password"),
                        is_active=True,
                        is_premium=False
                    )
                    db.add(dev_user)
                    await db.commit()
                    await db.refresh(dev_user)
                    logger.info(f"✅ DEV_AUTH_BYPASS: utilisateur de dev créé - id={dev_user.id}, email={dev_user.email}")
                    return dev_user
                    
            except (ValueError, TypeError) as e:
                logger.warning(f"⚠️ DEV_AUTH_BYPASS: X-Dev-User-Id n'est pas un UUID valide: {x_dev_user_id}, erreur: {e}")
                # Si le header n'est pas valide, continuer vers JWT
    
    # Mode normal: JWT (si bypass non activé ou header manquant)
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

