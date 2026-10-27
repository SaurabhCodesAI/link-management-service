from fastapi import APIRouter, Depends
from app.services.url import create_link
from app.schemas.url import UrlCreate,UrlResponse
from app.core.config import BASE_URL
from fastapi import HTTPException
from app.db.session import get_session

router = APIRouter()
@router.get("/health")
def health_check():
    return {"status" : "ok"}
@router.post("/urls")
def endpoint(data: UrlCreate, session=Depends(get_session)) -> UrlResponse:
    try:
        return create_link(data, BASE_URL, session)
    except ValueError:
        raise HTTPException(status_code = 409,
        detail = "alias already exists",)
