from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import Column, DateTime, JSON, Integer, Float, REAL
from sqlalchemy.sql import func
from sqlalchemy.types import ARRAY, FLOAT

base = declarative_base()

class Tracks(base):  
    __tablename__ = 'map_tracks'

    track_id = Column(Integer, primary_key=True, index=True)
    coordinates = Column(JSON)
    start_points = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
