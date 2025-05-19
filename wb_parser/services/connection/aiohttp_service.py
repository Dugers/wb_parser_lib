import json
from typing import Any, Dict, Optional
from aiohttp import ClientSession, ClientResponse

from .schemas import Response
from .base import AsyncConnectionBase
from .exceptions import RequestException, ParseResponseException

from logging import getLogger

logger = getLogger(__name__)

class AIOHTTPConnection(AsyncConnectionBase):
    async def get(self, url: str) -> Response:
        logger.debug(f"GET | START | {url}")
        try:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    logger.debug(f"GET | RESPONSE-STATUS | {response.status}")
                    try:
                        response_serialized = Response(
                            status=response.status,
                            json=await self._parse_json_from_request(response)
                        )
                        logger.info(f"GET | RESPONSE-SERIALIZED | URL: {url} | {response_serialized}")
                        return response_serialized
                    except Exception as e:
                        logger.error(f"GET | ParseResponseException | URL: {url} | Exception: {e}")
                        raise ParseResponseException(*e.args)
        except Exception as e:
            logger.error(f"GET | RequestException | URL: {url} | Exception: {e}")
            raise RequestException(*e.args)
        
    async def _parse_json_from_request(self, response: ClientResponse) -> Optional[Dict[Any, Any]]:
        try:
            return json.loads(await response.text())
        except:
            return None