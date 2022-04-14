import email
from statistics import mode
from unicodedata import name
from sqlalchemy.orm import Session
from model import User
import model
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from schemas import UserIn, UserSchema

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


async def create_User(self, u: UserIn) -> UserSchema:
    user = UserSchema(Email=u.email, Full_Name=u.Full_Name,)
    values = {**user.dict}
    values.pop("id", None)
    query = users.insert().values(**values)
    user.id = await self.database.execute(query)
    return user

# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = model.User(
#         email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
