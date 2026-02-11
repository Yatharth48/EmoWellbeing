from datetime import datetime, timedelta
import secrets
from uuid import uuid4
from jose import jwt
from passlib.context import CryptContext
import os
import re
from fastapi import HTTPException

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
OAUTH_PASSWORD_PLACEHOLDER = "__OAUTH_GOOGLE__DO_NOT_USE__"


def hash_password(password: str) -> str:
    return pwd_context.hash(password.strip())


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain.strip(), hashed)


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()

    jti = str(uuid4())
    expire = datetime.utcnow() + expires_delta

    to_encode.update({
        "exp": expire,
        "jti": jti,
        "type": "access"
    })

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(user_id: int):
    token = secrets.token_urlsafe(64)
    expires_at = datetime.utcnow() + timedelta(days=7)

    return {
        "token": token,
        "expires_at": expires_at
    }

def validate_password(password: str):
    if len(password) < 8:
        raise HTTPException(400, "Password must be at least 8 characters")

    if not re.search(r"[A-Z]", password):
        raise HTTPException(400, "Password must contain an uppercase letter")

    if not re.search(r"[a-z]", password):
        raise HTTPException(400, "Password must contain a lowercase letter")

    if not re.search(r"[0-9]", password):
        raise HTTPException(400, "Password must contain a number")

    if not re.search(r"[!@#$%^&*]", password):
        raise HTTPException(400, "Password must contain a special character")
    