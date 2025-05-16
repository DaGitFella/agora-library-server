from fastapi import FastAPI
from agora_library_server.api.v1 import api_router

app = FastAPI(title="agora library API")

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
