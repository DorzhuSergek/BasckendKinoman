import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.environ.get(
    'postgres://lxibpfvqfvkyfe:deb5b2578513ccf55aee3a29927a7471dcb891e05b5dfb66d28371169e420162@ec2-52-3-200-138.compute-1.amazonaws.com:5432/db3vqjro4is23a')
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Zaverchu17@localhost:5432/KinoMan"
engine = create_engine(
    'postgresql://lxibpfvqfvkyfe:deb5b2578513ccf55aee3a29927a7471dcb891e05b5dfb66d28371169e420162@ec2-52-3-200-138.compute-1.amazonaws.com:5432/db3vqjro4is23a'
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
