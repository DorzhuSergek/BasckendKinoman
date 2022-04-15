from sqlalchemy.orm import Session
import model
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from schemas import User
from schemas import UserCreate
from core.security import hash_password


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
    new_user = User(
        Email=u.Email,
        Full_Name=u.Full_Name,
        Hashed_password=hash_password(u.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
