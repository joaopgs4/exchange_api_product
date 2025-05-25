#dbutils.py
from sqlalchemy.orm import Session
from typing import List
from models import *
from schemas import *


# Function to get a product by its uuid
# Input: UUID str
# Output: A product DTO
def get_product_by_id(db: Session, uuid: str) -> ProductReadDTO:
    product = db.query(Product).filter(Product.uuid == uuid).first()
    if product:
        return ProductReadDTO(
            product_uuid=product.uuid,
            name=product.name,
            price=product.price,
            unit=product.unit
        )
    return None


# Function to get all products
# Input: db
# Output: A list of ProductReadDTO
def get_all_products(db: Session) -> List[ProductReadDTO]:
    products = db.query(Product).all()
    return [
        ProductReadDTO(
            product_uuid=product.uuid,
            name=product.name,
            price=product.price,
            unit=product.unit
        )
        for product in products
    ]


# Function to delete a product by its uuid
# Input: UUID str
# Output: A product DTO of the deleted product
def delete_product_by_id(db: Session, uuid: str) -> ProductReadDTO:
    product = db.query(Product).filter(Product.uuid == uuid).first()
    if product is None:
        return None

    db.delete(product)
    db.commit()

    return ProductReadDTO(
        product_uuid=product.uuid,
        name=product.name,
        price=product.price,
        unit=product.unit
    )


# Function to create a product by DTOs
# Input: ProductCreateDTO
# Output: ProductReadDTO
def create_product(db: Session, productDTO: ProductCreateDTO) -> ProductReadDTO:
    product = Product(
        name=productDTO.name,
        price=productDTO.price,
        unit=productDTO.unit
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    return ProductReadDTO(
        product_uuid=product.uuid,
        name=product.name,
        price=product.price,
        unit=product.unit
    )
