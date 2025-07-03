import aiohttp
from fastapi import HTTPException

from src.config import Config


class AIAPI:
    def __init__(self):
        self.url = "https://router.huggingface.co/hf-inference/models"
        self.session: aiohttp.ClientSession | None = None

    async def init_session(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def moderation(self, image):
        await self.init_session()
        url = self.url + "/Falconsai/nsfw_image_detection"
        content = await image.read()
        headers = {
            "Authorization": f"Bearer {Config.api_key}",
            "Content-Type": image.content_type
        }
        async with self.session.post(url, data=content, headers=headers) as response:
            try:
                if response.status == 200:
                    result = await response.json()
                    scores = {item["label"]: item["score"] for item in result}
                    nsfw_score = scores.get("nsfw", 0)
                    return nsfw_score
                else:
                    error = await response.text()
                    raise HTTPException(
                        status_code=response.status, detail=f'Ошибка API {error}'
                    )
            finally:
                await self.close()


ai_api = AIAPI()
