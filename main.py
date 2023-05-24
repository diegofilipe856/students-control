from fastapi import FastAPI
from Controllers import *
import uvicorn

app = FastAPI(
    title="My first layered-FastAPI using SQLAlchemy"
)

for direction in routes:
    app.include_router(direction)


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=5600, reload=True)
