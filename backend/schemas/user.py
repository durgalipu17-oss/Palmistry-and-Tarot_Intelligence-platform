from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str 

class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    username: str
    email: str
    age: Optional[int] = None
    occupation: Optional[str] = None
    goals: Optional[str] = None
    interests: Optional[str] = None
    reading_style: Optional[str] = None
    zodiac: Optional[str] = None
    bio: Optional[str] = None
    
class PasswordUpdate(BaseModel):
    old_password: str
    new_password: str


    
