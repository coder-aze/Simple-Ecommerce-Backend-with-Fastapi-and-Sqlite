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
    prefix="/business",
    tags=['Business Page']
)

@router.post("/add",tags=["Business Page"], status_code=status.HTTP_201_CREATED)
def Add_Business(requests: schemas.Add_Business, db: Session=Depends(get_db),get_current_user: schemas.Add_User=Depends(auth_data.get_current_user)):
    new_store=models.Business(store_name=requests.store_name,owner=users.current_user)
    check_store=db.query(models.Business).filter(models.Business.store_name==requests.store_name, models.Business.owner==users.current_user).all()
    if len(check_store)>=1:
        return "This store already have in your account"
    else:
        db.add(new_store)
        db.commit()
        db.refresh(new_store)
        return new_store

@router.get("/get",response_model=List[schemas.Get_Business],tags=["Business Page"])
def Get_Business(db: Session=Depends(get_db)):
    return db.query(models.Business).all()

@router.delete("/delete",tags=["Business Page"])
def Delete_Business(requests: schemas.Delete_Business, db: Session=Depends(get_db),get_current_user: schemas.Add_User=Depends(auth_data.get_current_user)):
    check_store=db.query(models.Business).filter(models.Business.store_name==requests.store_name, models.Business.owner==users.current_user).all()
    if len(check_store)==0:
        return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Store Not Found",
    )
    check_product=db.query(models.Product).filter(models.Product.product_owner==check_store[0].store_name).all()
    if len(check_product)>0:
        db.query(models.Product).filter(models.Product.product_owner==check_store[0].store_name).delete()
        db.query(models.Business).filter(
            models.Business.store_name==check_store[0].store_name
            ).delete(synchronize_session=False)
        db.commit()
        return "Business and Products Successfully deleted"
    else:
        db.query(models.Business).filter(
            models.Business.store_name==check_store[0].store_name
            ).delete(synchronize_session=False)
        db.commit()
        return "Business Successfully deleted"