from fastapi import Depends, FastAPI
from .database import SessionLocal
from crud import get_Movie


app = FastAPI()


def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movies")
def getMovie():
    return get_Movie(Depends(get_bd))
