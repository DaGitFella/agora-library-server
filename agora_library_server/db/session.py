from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from agora_library_server.settings import Settings

engine = create_engine(Settings.DATABASE_URL, echo=False)
session_factory = sessionmaker(bind=engine)
