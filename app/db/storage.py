from app.models.url import Link
from sqlalchemy.exc import IntegrityError
def find_by_alias(alias, session):
    return session.get(Link, alias)

def save_link(alias, target_url, session):
    new_link = Link(alias=alias, target_url= str(target_url))
    session.add(new_link)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ValueError("alias already exists")