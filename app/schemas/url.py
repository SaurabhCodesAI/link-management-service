from pydantic import BaseModel, HttpUrl

class UrlCreate(BaseModel):
    target_url: HttpUrl
    alias: str | None = None 

class UrlResponse(BaseModel):
    target_url: HttpUrl
    alias: str
    shortened_url: str