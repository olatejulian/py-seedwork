from abc import ABC, abstractmethod
from typing import Generic, TypeVar

R = TypeVar("R")


class QueryHandler(Generic[R], ABC):
    @abstractmethod
    def execute(self) -> R:
        raise NotImplementedError()
