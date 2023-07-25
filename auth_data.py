from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
import schemas
import os 
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme=OAuth2PasswordBearer(tokenUrl="/user/login")

class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)
    
    def verify(hashed_password,plain_password):
        return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str=payload.get("sub")
        if email is None:
            raise credential_exception
        token_data=schemas.TokenData(email=email)
    except JWTError:
        raise credential_exception


def get_current_user(token: str = Depends(oauth_2_scheme)):
    credential_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token,credential_exception)
    







