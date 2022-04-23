from statistics import mode
from typing import Any, Dict
import jwt
from sqlalchemy.orm import Session
import model
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from schemas import User
from schemas import UserCreate
from core.security import hash_password
from schemas import CommentIn
from schemas import Comments
from core.security import JWTBearer, decode_access_token
from core.config import ALGORITHM, SECRET_KEY
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_all_Movies(db: Session):
    return db.query(model.Movie).all()


def get_all_User(db: Session):
    return db.query(model.User).all()


def get_all_comments(db: Session):
    return db.query(model.Comments).all()


def get_all_chat(db: Session):
    return db.query(model.Chat).all()


def get_popular_movies(db: Session):
    return db.query(model.Movie).filter(model.Movie.typeMovies == "Популярные").all()


def get_inTheCinema(db: Session):
    return db.query(model.Movie).filter(model.Movie.typeMovies == "Уже в кино").all()


def get_best_movies(db: Session):
    return db.query(model.Movie).filter(model.Movie.typeMovies == "Лучшие").all()


def get_id_movie(db: Session, id: int):
    return db.query(model.Movie).filter(model.Movie.id == id).all()


def get_chat_byId_movie(db: Session, id: int):
    return db.query(model.Chat).filter(model.Chat.MovieId == id).all()


def get_comment_byId_comm(db: Session, id: int):
    return db.query(model.Comments).filter(model.Comments.MovieId == id).all()


def create_user(db: Session, u: UserCreate) -> User:
    new_user = model.User(
        Email=u.Email,
        Full_Name=u.Full_Name,
        Hashed_password=hash_password(u.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_by_email(db: Session, email: str) -> User:
    return db.query(model.User).filter(model.User.Email == email).first()


def create_comment(db: Session, user_id: int, c: CommentIn, movie_id: int) -> schemas.Comments:
    comment = model.Comments(
        text=c.text,
        UserId=user_id,
        MovieId=movie_id,
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def decode_access_token(db: Session, token: str):
    try:
        encode_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.JWSError:
        return None
    return encode_jwt


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        exp = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid auth token")
        if credentials:
            token = decode_access_token(credentials.credentials)
            if token is None:
                raise exp
            return credentials.credentials
        else:
            raise exp
