from typing import Generic, TypeVar, Any
from abc import ABC, abstractmethod

from ..value_object import EntityProps, NotificationErrorProps
from ..event import Event

Props = TypeVar("Props", bound=EntityProps)


class Entity(Generic[Props], ABC):
    class EventManager:
        def __init__(self):
            self.__events: list[Event]

        @property
        def events(self) -> list[Event]:
            return self.__events

        def add_event(self, event: Event) -> None:
            self.__events.append(event)

        def delete_events(self) -> None:
            self.__events.clear()

    class NotificationManager:
        def __init__(self):
            self.__errors: list[NotificationErrorProps] = []

        @property
        def errors(self) -> list[NotificationErrorProps]:
            return self.__errors

        def messages(self, context: str) -> str:
            message = ""

            for error in self.__errors:
                if error.context == context:
                    message += f"{error.context}: {error.message},"

            return message

        def add_error(self, context: str, message: str) -> None:
            error = NotificationErrorProps(context=context, message=message)
            self.__errors.append(error)

        def has_errors(self) -> bool:
            return len(self.__errors) > 0

        def remove_errors(self) -> None:
            self.__errors.clear()

    props: Props
    __events: EventManager
    __notification: NotificationManager

    @property
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        return self.props.dict()

    @property
    @abstractmethod
    def to_json(self) -> str:
        return self.props.json()
