from fastapi import FastAPI
from app.routers import points, polygons

app = FastAPI()
app.include_router(points.router)
app.include_router(polygons.router)
