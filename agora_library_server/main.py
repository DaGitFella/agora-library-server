from fastapi import FastAPI
from agora_library_server.api.v1 import api_router
from agora_library_server.db.base import table_registry
from agora_library_server.db.session import engine

app = FastAPI(title="agora library API")

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
def create_tables():
    table_registry.metadata.create_all(engine)