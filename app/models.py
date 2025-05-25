# models.py
import uuid
from sqlalchemy import (
    Column, String, Float
)
from sqlalchemy.orm import relationship, declarative_base
Base = declarative_base()

######################################################################
##### Uses SqlAlchemy bases for static objects; referenced in DB #####
######################################################################

class Product(Base):
    __tablename__ = 'product'
    
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(60), nullable=False, unique=True)
    price = Column(Float(8), nullable=False)
    unit = Column(String(12), nullable=False)

