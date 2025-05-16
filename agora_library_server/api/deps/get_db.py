from agora_library_server.db.session import session_factory


def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()
