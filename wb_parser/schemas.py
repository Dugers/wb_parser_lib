from typing import List, Optional
from pydantic import BaseModel

class ProductGet(BaseModel):
    imt_name: str
    description: Optional[str] = None

class ProductFind(BaseModel):
    id: int
    name: str

class ProductGetResponse(ProductGet):
    pass

class ProductFindResponseWrapper(BaseModel):
    products: List[ProductFind]

class ProductFindResponse(BaseModel):
    data: ProductFindResponseWrapper