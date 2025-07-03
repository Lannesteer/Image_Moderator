from fastapi import UploadFile, File

from src.moderator.exception import ModeratorException


async def validation_image(image: UploadFile = File(...)) -> UploadFile:
    if image.content_type not in ("image/jpeg", "image/png"):
        raise ModeratorException.ValidationError
    return image
