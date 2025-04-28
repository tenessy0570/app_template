from app.loggers.base import AbstractLogger
from app.repositories.base import AbstractRepository


class UserService:
    def __init__(
            self,
            logger: AbstractLogger,
            repo: AbstractRepository
    ):
        self.logger = logger
        self.repo = repo

    def create_new(self, *args, **kwargs) -> int:
        ...
