from fastapi import APIRouter
from app.db.config import SessionDep
from app.product.services import create_product
from app.product.schemas import ProductBase, ProductRead

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/create", response_model=ProductRead)
async def product_create(session: SessionDep, product: ProductBase):
    return await create_product(session, product)