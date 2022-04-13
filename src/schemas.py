from datetime import date
from tkinter import Image
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import List


class MovieBase(BaseModel):
    Name: str
    Poster: str
    Genre: str
    RaitingIMDb: str
    sinopsis: str
    Trailer: str
    Vote_from_user: str
    typeMovies: str


class Movie(MovieBase):
    id: int
    full_name = str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ChatBase(BaseModel):
    movieId: int
    userID: int
    text: str


class Chat(ChatBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    full_name: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class CommentsBase(BaseModel):
    text: str
    movieId: int
    userId: List[User]


class Comments(CommentsBase):
    id: int
    user: List[User] = []

    class Config:
        orm_mode = True


class ActorBase(BaseModel):
    FullName: str
    Profile: str


class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class MovieSchema(MovieBase):
    actors: List[ActorBase]


class ActorSchema(ActorBase):
    movie: List[MovieBase]
