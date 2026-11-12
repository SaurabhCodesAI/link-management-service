from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.services.url import create_link, resolve_link
from app.schemas.url import UrlCreate,UrlResponse
from app.core.config import BASE_URL 
from app.db.session import get_session

router = APIRouter()

@router.post("/urls")
def endpoint(data: UrlCreate, session=Depends(get_session)) -> UrlResponse:
    try:
        return create_link(data, BASE_URL, session)
    except ValueError:
        raise HTTPException(status_code = 409,
        detail = "alias already exists",)
@router.get("/health")
def health_check():
    return {"status" : "ok"}

@router.get("/{alias}")
def redirect_to_url(alias, session=Depends(get_session)):
    try:
        result = resolve_link(alias, session)
    except ValueError:
        raise HTTPException(status_code = 404,
        detail = "alias not found")
    return RedirectResponse(url = result)

