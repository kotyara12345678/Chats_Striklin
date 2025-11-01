from sqlalchemy import func
from datetime import datetime
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncAttrs

database_url = "sqlite+aiosqlite:///db.sqlite3"
engine = create_async_engine(url=database_url)
async_session = async_sessionmaker(engine, class_=AsyncSession)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())


def async_session_maker():
    return None