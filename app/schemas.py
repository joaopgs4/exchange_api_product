# schemas.py
from typing import Optional
from pydantic import BaseModel, EmailStr

#########################################################################
##### Uses pydantic for cache/dynamic objects; not referenced in DB #####
#########################################################################

# Base JWT AuthToken model
class AuthToken(BaseModel):
    uuid: str
    username: str
    email: EmailStr
    role: Optional[str] = None
    exp: Optional[int] = None  # Optional expiry (timestamp) for the JWT

    class Config:
        extra = "allow"

class ProductCreateDTO(BaseModel):
    name: str
    price: float
    unit: str

class ProductReadDTO(BaseModel):
    product_uuid: str
    name: str
    price: float
    unit: str
