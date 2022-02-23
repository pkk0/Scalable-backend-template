from fastapi import APIRouter, status, HTTPException
from app.database.loader import Session
from app.schemas import *
import app.crud as crud

#
# Sample router file
#

router = APIRouter(
    prefix='/books',
    tags=['books']
)

NOT_FOUND_RESPONSE = {
    404: {
        'content': {
            'application/json': {
                'example': {
                    'detail': 'Book not found.'
                }
            }
        }
    }
}

@router.post( 
    path='/',
    response_model=BookInDatabase,
    status_code=status.HTTP_201_CREATED
)
async def create_book_enpoint(in_params: BookCreate):
    return await crud.create_book(Session(), in_params)


@router.get(
    path='/',
    response_model=list[BookInDatabase]
)
async def read_books_enpoint():
    return await crud.read_books(Session())


@router.get(
    path='/{id}',
    response_model=BookInDatabase,
    responses=NOT_FOUND_RESPONSE
)
async def read_book_enpoint(id: int):
    book = await crud.read_book(Session(), id)

    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Book not found.')
    
    return book


@router.put(
    path='/{id}',
    response_model=BookInDatabase,
    responses=NOT_FOUND_RESPONSE
)
async def update_book_enpoint(id: int, in_params: BookUpdate):
    book = await crud.update_book(Session(), id, in_params)

    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Book not found.')

    return book


@router.delete(
    path='/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses=NOT_FOUND_RESPONSE
)
async def delete_book_enpoint(id: int):
    if not await crud.delete_book(Session(), id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Book not found.')