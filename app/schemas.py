# schemas.py
from typing import Optional
from pydantic import BaseModel, EmailStr

#########################################################################
##### Uses pydantic for cache/dynamic objects; not referenced in DB #####
#########################################################################

#Base JWT AuthToken model
class AuthToken(BaseModel):
    id : int
    username : str
    email : str
    role : Optional[str] = None
    exp : Optional[int] = None  # Optional expiry (timestamp) for the JWT

    # Allow any additional fields
    class Config:
        extra = "allow"

class ProductCreateDTO(BaseModel):
    name : str
    price : float
    unit : str

class ProductReadDTO(BaseModel):
    id : int
    name : str
    price : float
    unit : str
