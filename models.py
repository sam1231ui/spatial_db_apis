from sqlalchemy import Column, Integer
from geoalchemy2 import Geometry
from app.database import Base

class PointData(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(Geometry("POINT", srid=4326))

class PolygonData(Base):
    __tablename__ = "polygons"
    id = Column(Integer, primary_key=True, index=True)
    area = Column(Geometry("POLYGON", srid=4326))
