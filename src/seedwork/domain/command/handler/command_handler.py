from abc import ABC, abstractmethod


class CommandHandler(ABC):
    @abstractmethod
    def execute():
        raise NotImplementedError()
