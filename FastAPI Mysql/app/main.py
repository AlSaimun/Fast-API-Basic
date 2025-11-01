from fastapi import FastAPI
from .product.routers import router as product_router

app = FastAPI()

app.include_router(product_router)
