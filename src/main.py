from datetime import date

from fastapi import FastAPI
from articles.schemas import Query
from articles.router import router as router_artcl

app = FastAPI()


app.include_router(router_artcl)
