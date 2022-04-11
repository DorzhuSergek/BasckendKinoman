from ast import Str
from enum import unique
from operator import index
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Movie (Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, unique=True, index=True)
    Poster = Column(String, unique=True, index=True)
    Genre = Column(Integer, ForeignKey=True, index=True)
    RaitingIMDb = Column(Float, unique=True, index=True)
    Sinopsis = Column(String, unique=True, index=True)
    Trailer = Column(String, unique=True, index=True)
    Vote_from_user = Column(String, unique=True, index=True)
    Chat = Column(Integer, unique=True, index=True)
    typeMovies = Column(String, unique=True, index=True)


class Genre(Base):
    __tablename__ = "Genre"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class GenreMovies(Base):
    __tablename__ = "Genre&Movies"
    id = Column(Integer, primary_key=True, index=True)
    idMovie = Column(Integer, ForeignKey("Movie.id"))
    idGenre = Column(Integer, ForeignKey("Genre.id"))
