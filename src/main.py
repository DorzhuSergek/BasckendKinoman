from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movies")
async def read_movies(db: Session = Depends(get_db)):
    movies = crud.get_all_Movies(db)
    return movies


@app.get("/user")
async def read_user(db: Session = Depends(get_db)):
    user = crud.get_all_User(db)
    return user


@app.get("/all_chats")
async def read_chat(db: Session = Depends(get_db)):
    chat = crud.get_all_chat(db)
    return chat


@app.get("/comments")
async def read_comments(db: Session = Depends(get_db)):
    comment = crud.get_all_comments(db)
    return comment


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/movies/popular")
async def popular_Film(db: SessionLocal = Depends(get_db)):
    popular = crud.get_popular_movies(db)
    return popular


@app.get("/movies/in_The_Cinema")
async def in_the_Cinema(db: SessionLocal = Depends(get_db)):
    inTheCinema = crud.get_inTheCinema(db)
    return inTheCinema


@app.get("/movies/best_Movies")
async def intheCinema(db: SessionLocal = Depends(get_db)):
    bestMovies = crud.get_best_movies(db)
    return bestMovies
