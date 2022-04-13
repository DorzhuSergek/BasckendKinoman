from ast import Str
from datetime import date
from typing import Text
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from database import Base


class Chat(Base):
    __tablename__ = "Chat"
    id = Column(Integer, primary_key=True, index=True)
    MovieId = Column(Integer)
    UserId = Column(Integer)
    Text = Column(String)


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    Full_Name = Column(String)
    Email = Column(String)
    Hashed_password = Column(String)
    Role = Column(String)
    comments = relationship("Comments", back_populates="owner")


class Comments (Base):
    __tablename__ = "Comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    MovieId = Column(Integer, ForeignKey("Movies.id"))
    UserId = Column(Integer, ForeignKey("UserId"))
    user = relationship("User", back_populates="comments")


class Movie(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, unique=True, index=True)
    Poster = Column(String, unique=True, index=True)
    Genre = Column(String, unique=True, index=True)
    RaitingIMDb = Column(String, unique=True, index=True)
    sinopsis = Column(String, unique=True, index=True)
    Trailer = Column(String, unique=True, index=True)
    Vote_from_user = Column(String, unique=True, index=True)
    typeMovies = Column(String, unique=True, index=True)
    actor = relationship("Actor", secondary="Actor_Movies",
                         back_populates="movies")


class Actor(Base):
    __tablename__ = "Actor"
    id = Column(Integer, primary_key=True, index=True)
    Full_Name = Column(String)
    profile = Column(String)
    movies = relationship(
        "Movie", secondary="Actor_Movies", back_populates="actor")
    movie = relationship("Actor", secondary="Actor_Movies",
                         back_populates="movies")


class MoviesActor(Base):
    __tablename__ = "Actor_Movies"
    MovieID = Column(ForeignKey("Movies.id"), primary_key=True)
    ActorId = Column(ForeignKey("Actor.id"), primary_key=True)
    movie = relationship("Movie", back_populates="movie")
    actor = relationship("Actor", back_populates="actor")
