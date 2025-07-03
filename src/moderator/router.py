from fastapi import APIRouter, UploadFile, File

from src.moderator.dependencies import validation_image
from src.moderator.schemas import ModerateResponse
from src.services.aiapi.ai_client import ai_api

router = APIRouter(tags=["Moderator | Check_image"])


@router.post("/moderate", response_model=ModerateResponse)
async def moderate(image: UploadFile = File(...)):
    valid_image = await validation_image(image)
    if valid_image:
        nsfw_score = await ai_api.moderation(valid_image)
        if nsfw_score > 0.7:
            return ModerateResponse(status="REJECTED", reason="NSFW content")
        else:
            return ModerateResponse(status="OK")
