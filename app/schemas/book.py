from pydantic import BaseModel

#
# Sample schema file, used in router and crud 
# for data validation and type annotations
#

class BookCreate(BaseModel):
    title: str
    author: str

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None

class BookInDatabase(BaseModel):
    id: int
    title: str
    author: str
    class Config:
        orm_mode = True