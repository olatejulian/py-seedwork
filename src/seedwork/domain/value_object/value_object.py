from pydantic import BaseModel
from abc import ABC


class ValueObject(BaseModel, ABC):
    pass
