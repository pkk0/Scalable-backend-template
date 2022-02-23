from os import getenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DB_HOST = getenv('DATABASE_HOST')
DB_USERNAME = getenv('DATABASE_USER')
DB_PASSWORD = getenv('DATABASE_PASSWORD')
DB_NAME = getenv('DATABASE_NAME')
DATABASE_URL = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

#
# For debugging SQL queries and connection pool uncoment line below.
# engine = create_async_engine(DATABASE_URL, future=True, echo=True, echo_pool='debug')
#
engine = create_async_engine(DATABASE_URL, future=True)
Session: AsyncSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession, future=True)