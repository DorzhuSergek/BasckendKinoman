from sqlalchemy.orm import Session
from . import models, schemas


def get_Movie(session):
    return session.query(models.Movie)
