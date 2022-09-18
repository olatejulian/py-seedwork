from abc import ABC, abstractmethod


class EventHandler(ABC):
    @abstractmethod
    def execute():
        raise NotImplementedError()
