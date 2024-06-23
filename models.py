from datetime import date
from pydantic import BaseModel


class Query(BaseModel):
    title: str
    date: date
