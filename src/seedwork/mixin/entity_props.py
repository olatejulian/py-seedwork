from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field

from base import BaseMixin


class EntityPropsMixin(BaseMixin):
    id: UUID = Field(default_factory=uuid4, allow_mutation=False)
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        exclude = ["__props", "__notification", "__events"]
        json_encoders = {datetime: lambda v: v.timestamp()}
