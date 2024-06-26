from datetime import date
from pydantic import BaseModel


class Query(BaseModel):
    title: str
    date: date

class Aricle(BaseModel):
    query: Query
    text: str
    date_update: date
