from fastapi import FastAPI
from database import engine
import models
import uvicorn
import users, business, products

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(users.router)
app.include_router(business.router)
app.include_router(products.router)

