from fastapi import FastAPI

app = FastAPI(title='agora_library.api')

app.get('/')
def read_root():
    return {'Message': 'Hello World!'}
