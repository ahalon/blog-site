from fastapi import FastAPI
from database import models
from database.database import engine
from routers import post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI app
app = FastAPI()
app.include_router(post.router)

# CORS configuration
origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Mount the images directory to serve uploaded images
app.mount("/images", StaticFiles(directory="images"), name="images")