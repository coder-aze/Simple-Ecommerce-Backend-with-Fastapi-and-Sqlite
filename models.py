from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"
    id=Column(Integer,primary_key=True,index=True, autoincrement=True)
    name=Column(String, ForeignKey("business.owner"), unique=True)
    email=Column(String)
    password=Column(String)
    conn_user_business = relationship("Business", back_populates="conn_business_user")


class Business(Base):
    __tablename__ = "business"
    id=Column(Integer,primary_key=True,index=True, autoincrement=True)
    store_name=Column(String, ForeignKey("product.product_owner"))
    owner=Column(String)
    conn_business_user=relationship("User", back_populates="conn_user_business")
    conn_business_product=relationship("Product", back_populates="conn_product_business")

class Product(Base):
    __tablename__ = "product"
    id=Column(Integer,primary_key=True,index=True, autoincrement=True)
    product_name=Column(String)
    product_price=Column(Integer)
    product_owner=Column(String)
    conn_product_business=relationship("Business", back_populates="conn_business_product")

    


