from pydantic import BaseModel
from typing import List

class PointCreate(BaseModel):
    coordinates: List[float]  # [longitude, latitude]

class PolygonCreate(BaseModel):
    coordinates: List[List[float]]  # [[lng, lat], [lng, lat], ...]
