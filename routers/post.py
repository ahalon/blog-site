import shutil
from fastapi import FastAPI, APIRouter, Depends, UploadFile, File
from database.database import get_db
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from database import db_post
import string
import random

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.post('')
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)

@router.get('')
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_post.delete(id, db)

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    # Implementation for uploading image
    letter = string.ascii_letters
    random_string = ''.join(random.choice(letter) for i in range(10))
    new = f'_{random_string}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {'filepath': path}