from typing import List
from pydantic import BaseModel

###########---USER SCHEMAS---###########
class Login_User(BaseModel):
    email: str
    password: str
    class Config():
        orm_mode = True

class Add_User(BaseModel):
    name: str
    email: str
    password: str
    class Config():
        orm_mode = True

class Get_User(BaseModel):
    name: str
    class Config():
        orm_mode = True
########################################


###########---BUSINESS SCHEMAS---###########
class Add_Business(BaseModel):
    store_name: str
    class Config():
        orm_mode = True

class Get_Only_Business_Name(BaseModel):
    store_name: str
    class Config():
        orm_mode = True

class Get_Business(BaseModel):
    store_name: str
    conn_business_user: List[Add_User]=[]
    class Config():
        orm_mode = True

class Delete_Business(BaseModel):
    store_name: str
    class Config():
        orm_mode = True
########################################


###########---PRODUCT SCHEMAS---###########
class Add_Product(BaseModel):
    product_name: str
    product_price: str
    product_owner: str

class Get_Product(BaseModel):
    product_name: str
    product_price: str
    conn_product_business: List[Get_Only_Business_Name]=[]
    class Config():
        orm_mode = True

class Del_Product(BaseModel):
    product_name: str
    product_owner: str
    class Config():
        orm_mode = True

class Update_Product(BaseModel):
    product_name: str
    product_price: str
    product_owner: str
    new_product_name: str
    new_product_price: str
########################################


###########---TOKEN SCHEMAS---###########
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str or None = None
########################################
