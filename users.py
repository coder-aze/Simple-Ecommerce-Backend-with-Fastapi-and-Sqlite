from fastapi import FastAPI,Depends,HTTPException,status,APIRouter
from database import engine, get_db
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
import auth_data
import schemas
import models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
)

current_user=None

@router.post("/login",tags=["Login Page"])
def Login(requests: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==requests.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not auth_data.Hash.verify(user.password,requests.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    access_token = auth_data.create_access_token(data={"sub": user.email})
    global current_user
    current_user=user.name
    return {"access_token": access_token, "token_type": "bearer"}
    
@router.post("/registration",tags=["Login Page"], status_code=status.HTTP_201_CREATED)
def Registration(requests: schemas.Add_User, db: Session=Depends(get_db)):
    new_user=models.User(name=requests.name,email=requests.email,password=auth_data.Hash.bcrypt(requests.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users", tags=["Get Users Page"], response_model=List[schemas.Get_User])
def Get_Users(db: Session=Depends(get_db),get_current_user: schemas.Add_User=Depends(auth_data.get_current_user)):
    return db.query(models.User).all()
