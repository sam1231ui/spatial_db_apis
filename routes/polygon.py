from shapely.geometry import Polygon
from app.schemas import PolygonCreate
from app.models import PolygonData

@router.post("/polygons/")
async def create_polygon(data: PolygonCreate, db: AsyncSession = Depends(get_db)):
    polygon = from_shape(Polygon(data.coordinates), srid=4326)
    stmt = insert(PolygonData).values(area=polygon)
    await db.execute(stmt)
    await db.commit()
    return {"status": "polygon stored"}

@router.get("/polygons/")
async def get_all_polygons(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PolygonData))
    return result.scalars().all()
