from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class RegisterRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    age: int
    blood_type: constr(min_length=1, max_length=10)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class CheckupRequest(BaseModel):
    questions: list[str]

class CheckupResponse(BaseModel):
    score: float
    response: str

class Doctor(BaseModel):
    id: str
    name: str
    department: str
    specialty: str
    experience: int

class DocListResponse(BaseModel):
    doctors: list[Doctor]

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str
