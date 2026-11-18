from pydantic import BaseModel, HttpUrl, Field, field_validator
RESERVED_ALIASES = {"health", "docs", "redoc", "urls"}
class UrlCreate(BaseModel):
    target_url: HttpUrl
    alias: str | None = Field(default=None, min_length = 2, max_length = 12, pattern="^[A-Za-z0-9]+$")

    @field_validator("alias")
    @classmethod
    def alias_must_not_be_reserved(cls, value):
        if value in RESERVED_ALIASES:
            raise ValueError("reserved words can't be used as alias")
        return value

class UrlResponse(BaseModel):
    target_url: HttpUrl
    alias: str
    shortened_url: str