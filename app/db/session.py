from sqlalchemy.orm import sessionmaker
from app.db.engine import engine

SessionLocal = sessionmaker(bind=engine)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
