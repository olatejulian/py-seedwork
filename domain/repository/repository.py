from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from ..entity import Entity

E = TypeVar("E", bound=Entity)


class Repository(Generic[E], ABC):
    @abstractmethod
    def create(self, entity: E) -> E:
        raise NotImplementedError()

    @abstractmethod
    def read(self, id: UUID) -> E:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity: E) -> E:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: UUID) -> None:
        raise NotImplementedError()
