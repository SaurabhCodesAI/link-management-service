from fastapi import FastAPI
from app.api.url import router
app = FastAPI()
app.include_router(router)
