from .database import Base
from sqlalchemy import Column, Integer, String, Text

class DbPost(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String, index=True)
    content = Column(Text)
    creator = Column(String)
    timestamp = Column(String)