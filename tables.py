import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Measurement(Base):
    __tablename__ = "measurement"
    id = Column(Integer, primary_key=True)
    stations = Column(String(255))
    date = Column(String(255))
    prcp = Column(Float)
    tobs = Column(Float)
