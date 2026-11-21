from app.models.url import Link
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

def find_by_alias(alias, session):
    return session.get(Link, alias)

def save_link(alias, target_url, session):
    new_link = Link(alias=alias, target_url= str(target_url))
    session.add(new_link)
    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        if isinstance(error.orig, UniqueViolation):
            raise ValueError("alias already exists")
        raise