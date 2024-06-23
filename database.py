from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date

class BaseModel(DeclarativeBase):
    pass

class Query(BaseModel):
    __tablename__ = 'query'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    date: Mapped[date]


engine = create_async_engine('sqlite+aiosqlite:///task.db')

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)