from sqlalchemy.orm import Session

import model


def get_all_Movies(db: Session):
    return db.query(model.Movie).all()
