from sqlalchemy.orm import Session
from ..models import models_user
from ..schemas import schema_users, schema_token
from passlib.context import CryptContext
from ..dependencies import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM \
, get_db, oauth2_scheme
from datetime import timedelta, datetime, timezone
from fastapi import Depends, HTTPException, status
from ..database import SessionLocal
import jwt
from jwt.exceptions import InvalidTokenError


pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
        return db.query(models_user.User).filter(models_user.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
        return db.query(models_user.User).filter(models_user.User.username == username).first()

def get_user_by_email(db: Session, email: str):
        return db.query(models_user.User).filter(models_user.User.email == email).first()

def hash_password(password: str):
        return pwd_content.hash(password)

def verify_password(plain_password, hashed_password):
        return pwd_content.verify(plain_password, hashed_password)

def authenticate_user(db: get_db, username: str, password: str):
        user = get_user_by_username(db=db, username=username)
        if not user:
               return False
        the_password = verify_password(password, user.hashed_password)
        if not the_password:
               return False
        return user
def create_access_token(data: dict, expire_timdelta: timedelta | None = None):
        to_encode = data.copy()

        if expire_timdelta:
                expire = datetime.now(timezone.utc) + expire_timdelta
        else:
                expire = datetime.now(timedelta.utc) + timedelta(minutes=15)

        to_encode['exp'] = expire
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
        return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):

        credential_error = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
                                )
        try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                username: str = payload.get('sub')
                if username is None:
                        raise credential_error
                token_data = schema_token.TokenData(username=username)

        except InvalidTokenError:
                raise credential_error

        user = get_user_by_username(SessionLocal(), username=token_data.username)

        if user is None:
                return credential_error
        return user

def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models_user.User).offset(skip).limit(limit).all()


def add_user(db: Session, user: schema_users.UserCreate):
        hashed_password = hash_password(user.password)
        db_user = models_user.User(
                first_name=user.first_name,
                last_name=user.last_name,
                hashed_password=hashed_password,
                email=user.email,
                username=user.username)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


def edit_user(db:Session, user_id: int, user:schema_users.UserUpdate):
        db_user = db.query(models_user.User).filter(models_user.User.id == user_id).first()
        user_dict = user.dict()

        for key, value in user_dict.items():
                setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user

def remove_user(db: Session, user_id: int):
        db_user = db.query(models_user.User).filter(models_user.User.id == user_id).first()
        db.delete(db_user)
        db.commit()
        return {}

