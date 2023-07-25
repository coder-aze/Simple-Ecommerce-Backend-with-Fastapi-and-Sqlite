from fastapi import FastAPI,Depends,HTTPException,status,APIRouter
from database import engine, get_db
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
import auth_data
import schemas
import models
from sqlalchemy.orm import Session
import users

router = APIRouter(
    prefix="/products",
    tags=['Product Page']
)


@router.post("/add",tags=["Product Page"], status_code=status.HTTP_201_CREATED)
def Add_Products(requests: schemas.Add_Product, db: Session=Depends(get_db),get_current_user: schemas.Add_User=Depends(auth_data.get_current_user)):
    check_store_product=db.query(models.Business).filter(models.Business.store_name==requests.product_owner, models.Business.owner==users.current_user).all() 
    if len(check_store_product)>1 or len(check_store_product)==0:
        return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Store Not Found",
    )
    else:
        new_product=models.Product(product_name=requests.product_name,product_price=requests.product_price,product_owner=requests.product_owner)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
        
@router.get("/get",response_model=List[schemas.Get_Product],tags=["Product Page"])
def Get_Products(db: Session=Depends(get_db)):
    return db.query(models.Product).all()

@router.delete("/delete",tags=["Product Page"])
def Delete_Products(requests: schemas.Del_Product, db: Session=Depends(get_db), get_current_user: schemas.Add_User=Depends(auth_data.get_current_user)):
    check_store=db.query(models.Business).filter(models.Business.store_name==requests.product_owner, models.Business.owner==users.current_user).all()
    if len(check_store)==0:
        return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Store Not Found",
    )
    check_product_name=db.query(models.Product).filter(models.Product.product_name==requests.product_name, models.Product.product_owner==check_store[0].store_name).all()
    if len(check_product_name)==0:
        return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product Not Found",
    )
    else:
        db.query(models.Product).filter(
            models.Product.product_name==requests.product_name,
            models.Product.product_owner==check_store[0].store_name
            ).delete(synchronize_session=False)
        db.commit()
        return "Product Succesfuly deleted"

@router.put("/update",tags=["Product Page"], status_code=status.HTTP_202_ACCEPTED)
def Update_Products(requests: schemas.Update_Product, db: Session=Depends(get_db), get_current_user: schemas.Add_User=Depends(auth_data.get_current_user)):
    check_store=db.query(models.Business).filter(models.Business.store_name==requests.product_owner, models.Business.owner==users.current_user).all()
    if len(check_store)==0:
        return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Store Not Found",
    )
    check_product_name=db.query(models.Product).filter(models.Product.product_name==requests.product_name, models.Product.product_owner==check_store[0].store_name).all()
    if len(check_product_name)==0:
        return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product Not Found",
    )
    else:
        db.query(models.Product).filter(
            models.Product.product_name==requests.product_name,
            ).update({"product_name":requests.new_product_name,"product_price":requests.new_product_price})
        db.commit()
        return "Product Succesfuly Updated"
