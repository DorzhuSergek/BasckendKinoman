from ast import Str
from datetime import date
import datetime
from typing import Text
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.ext.associationproxy import association_proxy


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
    comments = relationship("Comments", back_populates="movie")
    chat = relationship("Chat", back_populates="movie")
    actor = relationship("MoviesActor",
                         back_populates="movie")


class Comments (Base):
    __tablename__ = "Comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    MovieId = Column(Integer, ForeignKey("Movies.id"))
    UserId = Column(Integer, ForeignKey("User.id"))
    user = relationship("User", back_populates="comments")
    movie = relationship("Movie", back_populates="comments")


class Chat(Base):
    __tablename__ = "Chat"
    id = Column(Integer, primary_key=True, index=True)
    MovieId = Column(Integer, ForeignKey("Movies.id"))
    UserId = Column(Integer, ForeignKey("User.id"))
    Text = Column(String)
    user = relationship("User", back_populates="chat")
    movie = relationship("Movie", back_populates="chat")


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    Full_Name = Column(String)
    Email = Column(String)
    Hashed_password = Column(String)
    Role = Column(String)
    comments = relationship("Comments", back_populates="user")
    chat = relationship("Chat", back_populates="user")


class Actor(Base):
    __tablename__ = "Actor"
    id = Column(Integer, primary_key=True, index=True)
    Full_Name = Column(String)
    profile = Column(String)
    movie = relationship("MoviesActor",
                         back_populates="actor")


class MoviesActor(Base):
    __tablename__ = "Actor_Movies"
    MovieId = Column(ForeignKey("Movies.id"), primary_key=True)
    ActorName = Column(ForeignKey("Actor.id"), primary_key=True)
    movie = relationship("Movie", back_populates="actor")
    actor = relationship("Actor", back_populates="movie")

    # proxies
    author_name = association_proxy(
        target_collection='actor', attr='Full_Name')
    book_title = association_proxy(target_collection='movie', attr='name')
