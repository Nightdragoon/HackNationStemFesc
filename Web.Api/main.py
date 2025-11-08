from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine("mysql+pymysql://upiw3mqa58obep4h:VMqMoO6MuFgXjBt6ddl@b96lcxztraqbollhfyj6-mysql.services.clever-cloud.com:20670/b96lcxztraqbollhfyj6")

Base = automap_base()

# Reflect the database schema and prepare the base
Base.prepare(autoload_with=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

