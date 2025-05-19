from typing import Any, Dict, Optional
from pydantic import BaseModel

class Response(BaseModel):
    status: int
    json: Optional[Dict[Any, Any]] = None