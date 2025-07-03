from dataclasses import dataclass

from fastapi import HTTPException


@dataclass
class ModeratorException:
    ValidationError = HTTPException(status_code=400, detail="Поддерживаются только JPG и PNG")
