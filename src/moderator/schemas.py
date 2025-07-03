from typing import Optional

from pydantic import BaseModel


class ModerateResponse(BaseModel):
    status: str
    reason: Optional[str] = None
