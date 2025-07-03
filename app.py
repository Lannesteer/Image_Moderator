import uvicorn
from fastapi import FastAPI
from src.moderator.router import router as moderator_router

app = FastAPI(title="Image_Moderator")

app.include_router(moderator_router)

if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)
