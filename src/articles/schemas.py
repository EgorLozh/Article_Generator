from datetime import date
from pydantic import BaseModel, Field
from datetime import datetime


class Query(BaseModel):
    id: int
    title: str
    src_url: str
    update_at: datetime

class QueryCreate(BaseModel):
    title: str
    src_url: str
    update_at: datetime = Field(default_factory=datetime.now)

class Aricle(BaseModel):
    id: int
    query: Query
    text: str
    image: str | None
    update_at: datetime

class ArticleCreate(BaseModel):
    query_id: int
    text: str
    image: str | None
    update_at: datetime = Field(default_factory=datetime.now)
