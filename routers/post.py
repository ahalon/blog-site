from fastapi import FastAPI, APIRouter, Depends
from database.database import get_db
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from database import db_post

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