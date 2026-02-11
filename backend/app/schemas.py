from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# =========================
# AUTH SCHEMAS
# =========================

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


# =========================
# CHAT SCHEMAS
# =========================

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    id: int
    message: str
    response: str
    sentiment: str
    confidence: float
    timestamp: datetime

    class Config:
        from_attributes = True


# =========================
# MOOD SCHEMAS
# =========================

class MoodCheckIn(BaseModel):
    mood: str
    note: Optional[str] = None


# =========================
# CONTACT SCHEMAS
# =========================

class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    message: str
