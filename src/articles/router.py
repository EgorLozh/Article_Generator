from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from articles.models import Article
from database import get_async_session

router = APIRouter(
    prefix='/articles',
    tags=['Articles']
)

@router.get('/')
async def get_articles(session: AsyncSession = Depends(get_async_session)):
    stmt = select(Article)
    result = await session.execute(stmt)
    articles = result.scalars().all()
    if not articles:
        raise HTTPException(status_code=404, detail="No articles found")
    return articles

@router.get('/detail/{article_id}')
async def get_detail_article(article_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(Article).where(Article.id == article_id)
    result = await session.execute(stmt)
    article = result.scalars().first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article
