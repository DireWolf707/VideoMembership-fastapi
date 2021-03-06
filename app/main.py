from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table
from . import config,db
from .users.models import User

#settings = config.get_settings()
DB_SESSION = None

app = FastAPI()

@app.on_event("startup")
def on_startup():
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)

@app.get("/")
def homepage():
    return {"hello":"ASdasd"}