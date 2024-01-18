from abc import ABC, abstractmethod

from sqlalchemy import insert, select, delete, update
from sqlalchemy.orm import DeclarativeMeta

from db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError



class SQLAlchemyRepository(AbstractRepository):
    model: DeclarativeMeta = None
    join_models: [DeclarativeMeta] = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def edit_one(self, id: int, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            query = select(self.model) if self.join_models is None else select(self.model, *self.join_models)
            if self.join_models:
                for join_model in self.join_models:
                    query = query.join(join_model)

            res = await session.execute(query)
            return res

    async def find_one(self, filter_condition=None):
        async with async_session_maker() as session:
            query = select(self.model) if self.join_models is None else select(self.model, *self.join_models)
            if self.join_models:
                for join_model in self.join_models:
                    query = query.join(join_model)

            if filter_condition is not None:
                query = query.where(filter_condition)

            res = await session.execute(query)
            return res