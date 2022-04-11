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


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
