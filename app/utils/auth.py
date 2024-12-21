import os

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORYTHM = os.getenv("ALGORYTHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES)))
    to_encode.update({
        "exp": expire
    })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORYTHM)
