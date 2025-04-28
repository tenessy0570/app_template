import logging

from sqlalchemy.orm import Session

from app.database.config import SessionFactory
from app.loggers.base import AbstractLogger
from app import config
from app.repositories.base import AbstractRepository
from app.repositories.user import UserSQLAlchemyRepository
from app.services.user import UserService


def get_db_session() -> Session:
    return SessionFactory()


def get_logger() -> AbstractLogger:
    format_ = "[%(name)s][%(levelname)s][%(asctime)s] on line %(lineno)d - %(filename)s.%(funcName)s - %(message)s"
    logging.basicConfig(format=format_)
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    return logger


def get_user_repo(
        logger: AbstractLogger = get_logger(),
        session: Session = get_db_session()

) -> AbstractRepository:
    return UserSQLAlchemyRepository(
        logger=logger,
        session=session
    )


def get_user_service(
        logger: AbstractLogger = get_logger(),
        repo: AbstractRepository = get_user_repo()
) -> UserService:
    return UserService(
        logger=logger,
        repo=repo
    )
