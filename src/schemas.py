from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
