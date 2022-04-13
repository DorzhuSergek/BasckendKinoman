from ast import Str
from datetime import date
from typing import Text
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from database import Base
from sqlalchemy.ext.associationproxy import association_proxy


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


class Comments (Base):
    __tablename__ = "Comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    MovieId = Column(Integer)
    UserId = Column(Integer)


class MoviesActor(Base):
    __tablename__ = "Actor_Movies"
    MovieId = Column(ForeignKey("Movies.id"), primary_key=True)
    ActorName = Column(ForeignKey("Actor.id"), primary_key=True)
    movie = relationship("Movie", back_populates="actor")
    actor = relationship("Actor", back_populates="movie")


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
    actor = relationship("MoviesActor",
                         back_populates="movie")


class Actor(Base):
    __tablename__ = "Actor"
    id = Column(Integer, primary_key=True, index=True)
    Full_Name = Column(String)
    profile = Column(String)
    movie = relationship("MoviesActor",
                         back_populates="actor")
