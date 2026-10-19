from fastapi import APIRouter
from app.services.url import create_link
from app.schemas.url import UrlCreate,UrlResponse
from app.core.config import BASE_URL
from fastapi import HTTPException
router = APIRouter()
@router.get("/health")
def health_check():
    return {"status" : "ok"}
@router.post("/urls")
def endpoint(data: UrlCreate,) -> UrlResponse:
    try:
        return create_link(data, BASE_URL)
    except ValueError:
        raise HTTPException(status_code = 409,
        detail = "alias already exists",)
