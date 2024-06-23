from datetime import date

from fastapi import FastAPI
from models import Query

app = FastAPI()


query = Query(title='Ураа ГОООЛ', date=date.today())
@app.get("/")
def get_home():
    return query