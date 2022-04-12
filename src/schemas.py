from datetime import date
from tkinter import Image
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import List


class MovieBase(BaseModel):
    name: str
    poster: str
    genre: str
    raitingIMDb: str
    sinopsis: str
    trailer: str
    vote_from_user: str
    typeMovies: str


class Movie(MovieBase):
    id: int
    full_name = str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    full_name: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class ChatBase(BaseModel):
    movieId: int
    userID: int
    text: str


class Chat(ChatBase):
    id: int

    class Config:
        orm_mode = True


class CommentsBase(BaseModel):
    text: str
    movieId: int
    userId: List[User]


class Comments(CommentsBase):
    id: int

    class Config:
        orm_mode = True
