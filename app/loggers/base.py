from abc import ABC, abstractmethod


class AbstractLogger(ABC):
    @abstractmethod
    def debug(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def info(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def critical(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def error(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def exception(self, text: str):
        raise NotImplementedError
