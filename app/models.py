# models.py
from sqlalchemy import (
    Column, Integer, String, DateTime, Date, Time, ForeignKey, CheckConstraint, UniqueConstraint, SmallInteger,
    Float
)
from sqlalchemy.orm import relationship, declarative_base
Base = declarative_base()

######################################################################
##### Uses SqlAlchemy bases for static objects; referenced in DB #####
######################################################################

#Default password table for saving the user password as a hash256
#(Receives the hashed string)
class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False, unique=True)
    price = Column(Float(8), nullable=False, unique=True)
    unit = Column(String(12), nullable=False, unique=True)

