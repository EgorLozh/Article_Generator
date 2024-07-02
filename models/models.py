from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, MetaData


metadata = MetaData()
Model = declarative_base(metadata=metadata)

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
