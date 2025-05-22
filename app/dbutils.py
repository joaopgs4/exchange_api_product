from sqlalchemy.orm import Session
from typing import List
from models import *
from schemas import *
import hashlib
import os

PASS_SALT=os.getenv("PASS_SALT")
if PASS_SALT is None:
    raise ValueError("Environment variable PASS_SALT is not set.")

#Function to get a product by its id
#Input: ID int
#Output: A product DTO
def get_product_by_id(db: Session, id: str) -> ProductReadDTO:
    product = db.query(Product).filter(Product.id == id).first()
    if product:
        return ProductReadDTO(id=product.id, name=product.name, price=product.price, unit=product.unit)
    return None

#Function to get all products
#Input: db
#Output: A list of ProductReadDTO
def get_all_products(db: Session) -> List[ProductReadDTO]:
    products = db.query(Product).all()
    return [
        ProductReadDTO(
            id=product.id,
            name=product.name,
            price=product.price,
            unit=product.unit
        )
        for product in products
    ]

#Function to delete a product by its id
#Input: ID int
#Output: A product DTO of the deleted product
def delete_product_by_id(db: Session, id: str) -> ProductReadDTO:
    product = db.query(Product).filter(Product.id == id).first()
    
    if product is None:
        return None
    db.delete(product)
    db.commit()

    return ProductReadDTO(
        id=product.id,
        name=product.name,
        price=product.price,
        unit=product.unit
    )

#Function to create a product by DTOs
#Input: ProductCreateDTO
#Output: ProductReadDTO
def create_product(db: Session, productDTO: ProductCreateDTO) -> ProductReadDTO:
    product = Product(
        name=productDTO.name,
        price=productDTO.price,
        unit=productDTO.unit
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    return ProductReadDTO(id=product.id, name=product.name, price=product.price, unit=product.unit)