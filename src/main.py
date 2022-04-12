from fastapi import Depends, FastAPI, HTTPException
from fastapi_users_db_sqlalchemy import joinedload
from pip import List
from sqlalchemy.orm import Session

import crud
from database import SessionLocal, engine
import schemas
import model
from model import Movie
from schemas import MovieSchema
from model import Actor
app = FastAPI()


model.Base.metadata.create_all(bind=engine)


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


@app.get("/comments", response_model=List[schemas.Comments])
async def read_comments(db: Session = Depends(get_db)):
    comment = crud.get_all_comments(db)
    return comment


@app.get("/movies/popular")
async def popular_Film(db: SessionLocal = Depends(get_db)):
    popular = crud.get_popular_movies(db)
    return popular


@app.get("/movies/in_The_Cinema")
async def in_the_Cinema(db: SessionLocal = Depends(get_db)):
    inTheCinema = crud.get_inTheCinema(db)
    return inTheCinema


@app.get("/movies/best_Movies")
async def in_the_Cinema(db: SessionLocal = Depends(get_db)):
    bestMovies = crud.get_best_movies(db)
    return bestMovies


@app.get("/movies/{movie_id}")
async def get_movie_id(movie_id: int, db: SessionLocal = Depends(get_db)):
    mov = crud.get_id_movie(db, movie_id)
    return mov


@app.get("/chat/{movie_id}")
async def get_chat_id(movie_id: int, db: SessionLocal = Depends(get_db)):
    chat = crud.get_chat_byId_movie(db, movie_id)
    return chat


@app.get("/comments/{movie_id}")
async def get_comment_by_id_Movie(movie_id: int, db: SessionLocal = Depends(get_db)):
    itemComment = crud.get_comment_byId_comm(db, movie_id)
    return itemComment


# @app.get("/moviesss/{id}", response_model=MovieSchema,
#          response_model_exclude={'blurb'}, response_model_by_alias=False)
# async def get_book(id: int, db: Session = Depends(get_db)):
#     db_book = db.query(Movie).options(joinedload(Movie.actors)).\
#         where(Movie.id == id).one()
#     return db_book


@app.get("/books", response_model=List[MovieSchema])
async def get_books(db: Session = Depends(get_db)):
    db_books = db.query(Actor).options(joinedload(Actor.movies)).all()
    return db_books

# не работает хз почему(чини)


# @app.post("/users/", response_model=schemas.User)
# async def create_user(user: schemas.UserCreate, db: SessionLocal = Depends(get_db)):
#     db_user = crud.create_user(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
