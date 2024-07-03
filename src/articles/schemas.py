from datetime import date
from pydantic import BaseModel


class Query(BaseModel):
    id: int
    title: str
    src_url: str
    date: date


class Aricle(BaseModel):
    id: int
    query: Query
    text: str
    image: str | None
    date_update: date
