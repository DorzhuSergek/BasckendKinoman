from ctypes import Union
from pstats import Stats
from statistics import mode
import statistics
from typing import Any, Dict
from sqlalchemy.orm import Session
import model
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from schemas import User
from schemas import UserCreate
from core.security import hash_password
from schemas import CommentIn
from schemas import Comments
from core.security import JWTBearer, decode_access_token
from db import get_db


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


def create_comment(db: Session, user_id: int, j: CommentIn, movie_id: int):
    comment = Comments(
        text=j.text,
        UserId=user_id,
        MovieId=movie_id,
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


async def get_current_user(
    users: User = Depends(get_db),
    token: str = Depends(JWTBearer()),
) -> User:
    cred_exception = HTTPException(
        status_code=Stats.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await users.get_by_email(email=email)
    if user is None:
        return cred_exception
    return user
