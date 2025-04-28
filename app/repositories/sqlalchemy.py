from typing import Generic, TypeVar

from sqlalchemy import insert, select, delete, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.database.models import BaseModel
from app.exceptions.exceptions import DatabaseError, RepositoryError
from app.loggers.base import AbstractLogger
from app.repositories.base import AbstractRepository


F = TypeVar('F')


class SQLAlchemyRepository(AbstractRepository, Generic[F]):
    __model__ = BaseModel

    def __init__(self, session: Session, logger: AbstractLogger):
        self.session = session
        self.logger = logger
        super().__init__()

    def create_new(self, data: dict) -> int:
        added_object_id = None

        with self.session as session:
            try:
                result = session.execute(
                    insert(self.__model__)
                    .values(**data)
                    .returning(self.__model__.id)
                )
                added_object_id = result.scalar_one()
                session.commit()
            except IntegrityError:
                raise DatabaseError("Unique constraint failed, object already exists.")
            except (Exception, SQLAlchemyError) as exc:
                self.logger.exception(f"An error occurred while trying to create new object. "
                                      f"{self.__model__=}, {data=}")
                raise RepositoryError(str(exc))

        return added_object_id

    def fetch_all(self) -> list[F]:
        with self.session as s:
            query = select(self.__model__)
            result = s.execute(query).scalars().all()

        return result

    def fetch_by_id(self, id: int) -> F | None:
        with self.session as s:
            query = (
                select(self.__model__)
                .where(self.__model__.id == id)
            )

            result = s.execute(query).scalars().first()

        return result

    def delete_by_id(self, id: int):
        with self.session as session:
            query = (
                delete(self.__model__)
                .where(self.__model__.id == id)
            )

            try:
                session.execute(query)
                session.commit()
            except (Exception, SQLAlchemyError) as exc:
                self.logger.error(
                    f"An error occurred while trying to delete object. {exc=}, {self.__model__=}, {id=}"
                )
                raise RepositoryError(str(exc))

    def fetch_by_properties(self, properties: dict) -> list[F]:
        with self.session as s:
            query = select(self.__model__)

            for key, value in properties.items():
                query = query.where(getattr(self.__model__, key) == value)

            result: list = s.execute(query).scalars().all()

        return result

    def update_by_id(self, id: int, data: dict) -> F:
        with self.session as session:
            query = (
                update(self.__model__)
                .where(self.__model__.id == id)
                .values(**data)
            )

            try:
                session.execute(query)
                session.commit()
            except (Exception, SQLAlchemyError) as exc:
                self.logger.error(
                    f"An error occurred while trying to update object. {exc=}, {self.__model__=}, {id=}"
                )
                raise RepositoryError(str(exc))

            updated_object = self.session.execute(
                (
                    select(self.__model__)
                    .where(self.__model__.id == id)
                )
            ).scalars().first()

            return updated_object
