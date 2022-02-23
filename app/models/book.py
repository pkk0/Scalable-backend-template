from sqlalchemy import Column, Integer, String
from app.database.base import Base

#
# Sample SQLAlchemy ORM model
#
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    author = Column(String(100), nullable=False)