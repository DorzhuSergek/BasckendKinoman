from ast import Str
from datetime import date
from typing import Text
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


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
