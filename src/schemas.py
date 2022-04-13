from ast import Str
from datetime import date
from tkinter import Image
from pydantic import BaseModel, Field
from passlib.context import CryptContext
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, Query


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


class ChatBase(BaseModel):
    movieId: int
    userID: int
    text: str


class Chat(ChatBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    Email: str
    Full_Name: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class CommentsBase(BaseModel):
    text: str
    UserId: int
    MovieId: int


class CommentFilmBase(BaseModel):
    Name: str
    sinopsis: str


class CommentFilm(CommentFilmBase):
    pass

    class Config:
        orm_mode = True


class Comments(CommentsBase):
    id: int
    user: Optional[User]
    movie: CommentFilm

    class Config:
        orm_mode = True
