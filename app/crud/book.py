from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, update
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate, BookInDatabase

#
# Sample CRUD operations for book model
#

async def create_book(session: AsyncSession, in_params: BookCreate) -> BookInDatabase:
    async with session, session.begin():
        book = Book(**jsonable_encoder(in_params))
        session.add(book)

        return book

async def read_books(session: AsyncSession) -> list[BookInDatabase]:
    async with session:
        result = await session.execute(select(Book).order_by(Book.id))
        return result.scalars().all()

async def read_book(session: AsyncSession, id: int) -> BookInDatabase | None:
    async with session:
        result = await session.execute(select(Book).where(Book.id==id))

        return result.scalars().first()

async def update_book(session: AsyncSession, id: int, in_params: BookUpdate) -> BookInDatabase | None:
    async with session, session.begin():
        result = await session.execute(
            update(Book)
                .where(Book.id==id)
                .returning(Book)
                .values(**jsonable_encoder(in_params))
        )

        return result.first()

async def delete_book(session: AsyncSession, id: int) -> bool:
    async with session, session.begin():
        result = await session.execute(
            delete(Book)
                .where(Book.id==id)
        )

        return result.rowcount != 0