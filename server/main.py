#framework and library
from fastapi import FastAPI

#directory
from models.base import Base
from routes import auth
from database import engine

app = FastAPI()

app.include_router(auth.router, prefix='/auth')

Base.metadata.create_all(engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)