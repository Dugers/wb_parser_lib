from abc import ABC, abstractmethod

class UrlParserBase(ABC):
    @abstractmethod
    def parse_get_product_url(self, id: int) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def parse_find_products_url(self, query: str) -> str:
        raise NotImplementedError()