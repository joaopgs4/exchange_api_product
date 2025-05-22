# routers.py
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models import *
from schemas import *
from dbutils import *
from middleware import *
from database import get_db
from typing import List

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

###################################
##### Routers Functions Below #####
###################################

#Default function, change as needed
# @router.get("")
# async def root_func():
#     return {"message": "Root function ran!"}
    
#Function for product creation based on a json DTO
#Input: ProductCreateDTO, auth token
#Output: ProductReadDTO
@router.post("", response_model=ProductReadDTO, status_code=201)
async def product_register(payload: ProductCreateDTO, db: Session = Depends(get_db),
                           cookie: AuthToken = Depends(get_cookie_as_model)):
    try:        
        product = create_product(db, payload)
        return product
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

#Function for getting all products
#Input: auth token
#Output: List[ProductReadDTO]
@router.get("", response_model=List[ProductReadDTO], status_code=200)
async def show_all_products(db: Session = Depends(get_db),
                            cookie: AuthToken = Depends(get_cookie_as_model)):
    try:        
        products = get_all_products(db)
        return products
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Function for getting a product
#Input: id, auth token
#Output: ProductReadDTO
@router.get("/{id}", response_model=ProductReadDTO, status_code=200)
async def get_single_products(id: int, db: Session = Depends(get_db),
                              cookie: AuthToken = Depends(get_cookie_as_model)):
    try:        
        product = get_product_by_id(db, id)
        return product
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Function for deleting a product
#Input: id, auth token
#Output: ProductReadDTO
@router.delete("/{id}", response_model=ProductReadDTO, status_code=200)
async def delete_single_product(id: int, db: Session = Depends(get_db),
                                cookie: AuthToken = Depends(get_cookie_as_model)):
    try:        
        product = delete_product_by_id(db, id)
        return product
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))