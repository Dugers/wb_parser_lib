from typing import List
from .services.connection import AsyncConnectionBase
from .services.url_parser import UrlParserBase

from .schemas import *

class WbAsyncParser:
    def __init__(self, connection: AsyncConnectionBase, url_parser: UrlParserBase):
        self._connection = connection
        self._url_parser = url_parser

    async def get_product(self, id: int) -> ProductGet:
        url = self._url_parser.parse_get_product_url(id)
        response = await self._connection.get(url)
        return self._get_product_from_get_response(ProductGetResponse.model_validate(response.json))

    async def find_products(self, query: str) -> List[ProductFind]:
        url = self._url_parser.parse_find_products_url(query)
        response = await self._connection.get(url)
        return self._get_products_list_from_find_response(ProductFindResponse.model_validate(response.json))
    
    def _get_product_from_get_response(self, response_model: ProductGetResponse) -> ProductGet:
        return ProductGet(**response_model.model_dump())

    def _get_products_list_from_find_response(self, response_model: ProductFindResponse) -> List[ProductFind]:
        return response_model.data.products