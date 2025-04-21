from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from app.schemas import PointCreate
from app.models import PointData
from app.database import SessionLocal

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/points/")
async def create_point(data: PointCreate, db: AsyncSession = Depends(get_db)):
    point = from_shape(Point(data.coordinates), srid=4326)
    stmt = insert(PointData).values(location=point)
    await db.execute(stmt)
    await db.commit()
    return {"status": "point stored"}

@router.get("/points/")
async def get_all_points(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PointData))
    return result.scalars().all()
