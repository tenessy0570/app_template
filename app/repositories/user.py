from app.database.models import User
from app.repositories.sqlalchemy import SQLAlchemyRepository


class UserSQLAlchemyRepository(SQLAlchemyRepository[User]):
    __model__ = User
