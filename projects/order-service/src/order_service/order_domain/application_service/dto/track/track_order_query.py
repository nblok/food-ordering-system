from pydantic import BaseModel, ConfigDict
from uuid import UUID


class TrackOrderQuery(BaseModel):
    model_config = ConfigDict(frozen=True)
    tracking_id: UUID
