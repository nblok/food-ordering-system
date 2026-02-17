from pydantic import BaseModel
from uuid import UUID


class TrackOrderQuery(BaseModel, frozen=True):
    tracking_id: UUID
