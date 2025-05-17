from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from agora_library_server.core.settings import config

engine = create_engine(config.DATABASE_URL, echo=False)
session_factory = sessionmaker(bind=engine)


def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()
