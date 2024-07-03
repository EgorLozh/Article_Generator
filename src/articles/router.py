from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from articles.models import Query
from database import get_async_session

router = APIRouter(
    prefix='/articles',
    tags=['Articles']
)

@router.get('/')
async def get_articles(session: AsyncSession = Depends(get_async_session)):
    stmt = select(Query)
    result = await session.execute(stmt)
    return result.scalars().all()
