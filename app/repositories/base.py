from abc import abstractmethod, ABC
from typing import TypeVar

from _testcapi import Generic

T = TypeVar('T')


class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    def create_new(self, data: dict) -> int:
        raise NotImplementedError

    @abstractmethod
    def fetch_all(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def fetch_by_id(self, id: int) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def fetch_by_properties(self, data: dict) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def update_by_id(self, id: int, data: dict) -> T:
        raise NotImplementedError
