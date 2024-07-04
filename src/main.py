from datetime import date

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from articles.schemas import Query
from articles.router import router as router_artcl
from pages.router import router as router_pages

app = FastAPI()


app.include_router(router_artcl)
app.include_router(router_pages)

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
