from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Model(DeclarativeBase):
    pass

class Query(Model):
    __tablename__ = 'query'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(Date)

class Article(Model):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    query_id = Column(Integer, ForeignKey('query.id'))
    text = Column(String)
    date_update = Column(Date)


engine = create_async_engine('sqlite+aiosqlite:///task.db')

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)