from uuid import UUID

from pydantic import BaseModel, ConfigDict

from common.common_domain.valueobject.order_status import OrderStatus


class TrackOrderResponse(BaseModel):
    model_config = ConfigDict(frozen=True)
    tracking_id: UUID
    status: OrderStatus
    failure_messages: list[str] | None