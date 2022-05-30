import statistics
from tokenize import Token
from typing import Any, List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src import crud
from src.database import SessionLocal, engine
from src.schemas import Comments, Chat, UserCreate, CommentIn, UserSchema, UserUpdate
from fastapi.security import OAuth2PasswordBearer
from src import schemas
from src.model import Login, Token, User
from src.core.security import create_access_token, verify_password
from src.db import get_db
from src.core.security import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from src.schemas import ChatIn


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/")
async def root():
    return {"open": "/docs"}


@app.get("/movies")
async def read_movies(db: Session = Depends(get_db)):
    movies = crud.get_all_Movies(db)
    return movies


@app.get("/user")
async def read_user(db: Session = Depends(get_db)):
    user = crud.get_all_User(db)
    return user


@app.get("/all_chats", response_model=List[Chat])
async def read_chat(db: Session = Depends(get_db)):
    chat = crud.get_all_chat(db)
    return chat


@app.get("/comments", response_model=List[Comments])
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


@app.get("/comments/{movie_id}", response_model=List[Comments])
async def get_comment_by_id_Movie(movie_id: int, db: SessionLocal = Depends(get_db)):
    itemComment = crud.get_comment_byId_comm(db, movie_id)
    return itemComment


@app.post("/login", response_model=Token)
async def login(login: Login, db: SessionLocal = Depends(get_db)):
    user = await crud.get_by_email(db, login.email)
    if user is None or not verify_password(login.password, user.Hashed_password):
        raise HTTPException(status_code=statistics.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")

    return Token(
        access_token=create_access_token({"sub": user.Email}),
        token_type="Bearer"
    )


@app.get("/users/me")
async def read_items(token: str, db: SessionLocal = Depends(get_db)):
    userme = crud.decode_access_token(db, token)
    return userme


@app.post("/user", response_model=schemas.User)
def create_user(*, userIn: UserCreate, db: Session = Depends(get_db)) -> Any:
    user = crud.create_user(db=db, u=userIn)
    return user


@app.post("/comments/{MovieId}", response_model=Comments)
async def create_comment(*, c: CommentIn, movieId: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)) -> Any:
    return crud.create_comment(db=db, user_id=current_user.id, c=c, movie_id=movieId)


@app.post("/chat/", response_model=Chat)
async def create_message(*, c: ChatIn, db: SessionLocal = Depends(get_db), current_user: schemas.User = Depends(get_current_user)) -> Any:
    return crud.create_message(db=db, user_id=current_user.id, c=c)


@app.put("/update/user", response_model=schemas.User)
async def update_image(*, c: UserUpdate, db: SessionLocal = Depends(get_db), current_user: schemas.User = Depends(get_current_user)) -> Any:
    return crud.update_image(db, current_user, c)
