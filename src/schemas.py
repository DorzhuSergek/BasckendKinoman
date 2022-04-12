from datetime import date
from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    poster: str
    genre: str
    raitingIMDb: str
    sinopsis: str
    trailer: str
    vote_from_user: str
    typeMovies: str


class UserBase(BaseModel):
    name: str
    name: str
    login: str
    role: str
    password: str


class ChatBase(BaseModel):
    movieId: int
    userID: int
    text: str


class CommentsBase(BaseModel):
    text: str
    movieId: int
    userId: int


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Chat(ChatBase):
    id: int

    class Config:
        orm_mode = True


class Comments(CommentsBase):
    id: int

    class Config:
        orm_mode = True
