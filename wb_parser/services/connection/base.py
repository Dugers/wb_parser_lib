from abc import ABC, abstractmethod

from .schemas import Response

class AsyncConnectionBase(ABC):
    @abstractmethod
    async def get(self, url: str) -> Response:
        raise NotImplementedError()