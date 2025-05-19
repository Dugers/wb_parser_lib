from typing import Callable
from wb_parser.services.validator import url_validator, wb_id_validator, wb_query_validator
from wb_parser.config import WbV13FindParams, WbV13URLOffsets

from .base import UrlParserBase

from logging import getLogger

logger = getLogger(__name__)

class UrlParserV13(UrlParserBase):
    def __init__(self, base_url_get: str, base_url_find: str):
        log_validation(lambda : url_validator(base_url_get))
        log_validation(lambda : url_validator(base_url_find))

        self._base_url_get = base_url_get
        self._base_url_find = base_url_find

        logger.info(f"INIT | {base_url_get=} | {base_url_find=}")

    def parse_get_product_url(self, id: int) -> str:
        log_validation(lambda : wb_id_validator(id))

        product_vol = str(id)[:-WbV13URLOffsets.PRODUCT_VOL_FROM_ID_RIGHT_OFFSET]
        product_part = str(id)[:-WbV13URLOffsets.PRODUCT_PART_FROM_ID_RIGHT_OFFSET]
        url = f"{self._base_url_get}/vol{product_vol}/part{product_part}/{id}/info/ru/card.json"

        logger.info(f"PARSE | GET-PRODUCT | ID: {id} | {url}")

        return url
    
    def parse_find_products_url(self, query: str) -> str:
        log_validation(lambda: wb_query_validator(query))
        
        api_version = "v13"
        query_params = {}
        query_params["query"] = query
        query_params["resultset"] = WbV13FindParams.RESULTSET
        query_params["dest"] = WbV13FindParams.DEST
        query_params_value = "&".join(
            [f"{query_param_name}={query_params[query_param_name]}" for query_param_name in query_params.keys()])
        url = f"{self._base_url_find}/exactmatch/ru/common/{api_version}/search?{query_params_value}"
        
        logger.info(f"PARSE | FIND-PRODUCTS | QUERY: {query} | {url}")

        return url
    
def log_validation(func_validation: Callable[[], None]):
    try:
        func_validation()
    except Exception as e:
        logger.error(f"ValidationException | Exception: {e}")
        raise e