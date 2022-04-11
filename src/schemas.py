from sys import flags
from pydantic import BaseModel


class MovieBase(BaseModel):
    Name: str
    Poster: str
    Genre: str
    RaitingIMDb: float
    Sinopsis: str
    Trailer: str
    Vote_from_user: float
    Chat: str
    typeMovies: str


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
