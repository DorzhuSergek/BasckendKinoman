from pydantic import BaseModel, EmailStr, Field, validator, constr
from passlib.context import CryptContext
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, Query
import datetime


class MovieBase(BaseModel):
    Name: str
    Poster: str
    Genre: str
    RaitingIMDb: str
    sinopsis: str
    Trailer: str
    Vote_from_user: str
    typeMovies: str
    Background: str


class Movie(MovieBase):
    id: int
    full_name = str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    Email: str
    Full_Name: str
    avatar:  Optional[str] = None


class User (UserBase):
    id: int

    class Config:
        orm_mode = True


class CommentsBase(BaseModel):
    text: str


class CommentFilmBase(BaseModel):
    Name: str
    sinopsis: str


class CommentFilm(CommentFilmBase):
    pass

    class Config:
        orm_mode = True


class Comments(CommentsBase):
    user: Optional[User]
    movie: Optional[CommentFilm]
    UserId: int
    MovieId: int

    class Config:
        orm_mode = True


class ChatBase(BaseModel):
    Text: str


class Chat(ChatBase):
    id: int
    user: Optional[User]
    UserId: int
    time: datetime.datetime

    class Config:
        orm_mode = True


class ActorBase(BaseModel):
    FullName: str
    profile: str


class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class MovieSchema(MovieBase):
    Actors: List[ActorBase]


class ActorSchema(ActorBase):
    movie: List[MovieBase]


class UserCreate(BaseModel):
    Full_Name: str
    Email: EmailStr
    password: constr(min_length=5)
    password2: str

    @validator("password2")
    def password_mathc(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("passwords dont match")
        return v


class UserUpdate(BaseModel):
    avatar:  Optional[str] = None


class CommentIn(CommentsBase):
    pass


class ChatIn(ChatBase):
    pass


class UserSchema(User):

    class Config:
        orm_mode = True
