from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, MetaData, UniqueConstraint

metadata = MetaData()
Model = declarative_base(metadata=metadata)

class Query(Model):
    __tablename__ = 'query'
    id = Column(Integer, primary_key=True)
    src_url = Column(String, nullable=False)
    title = Column(String)
    update_at = Column(DateTime)
    __table_args__ = (UniqueConstraint('title', 'src_url'),)

class Article(Model):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    query_id = Column(Integer, ForeignKey('query.id'))
    text = Column(String)
    image = Column(String, nullable=True)
    update_at = Column(DateTime)
    __table_args__ = (UniqueConstraint('query_id'),)
