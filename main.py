from fastapi import FastAPI
from database import models
from database.database import engine
from routers import post

app = FastAPI()
app.include_router(post.router)


models.Base.metadata.create_all(bind=engine)

