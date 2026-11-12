from app.schemas.url import UrlCreate, UrlResponse
from app.db.storage import find_by_alias, save_link
from app.utils.helper import generate_identifier
def create_link(data: UrlCreate, base_url: str, session) -> UrlResponse:
    if data.alias is not None:
        existing = find_by_alias(data.alias, session)
        if existing is not None:
            raise ValueError("alias already exists")
        final_alias = data.alias
    else:
        candidate = generate_identifier()
        existing = find_by_alias(candidate, session)
        while existing is not None:
            candidate = generate_identifier()
            existing = find_by_alias(candidate, session)
        final_alias = candidate
    save_link(final_alias, data.target_url, session)
    shortened_url = base_url + "/" + final_alias
    return UrlResponse(
        target_url = data.target_url,
        alias = final_alias,
        shortened_url = shortened_url,
    )

def resolve_link(alias, session):
    result = find_by_alias(alias, session)

    if result is None:
        raise ValueError("alias not found")
    return result.target_url
