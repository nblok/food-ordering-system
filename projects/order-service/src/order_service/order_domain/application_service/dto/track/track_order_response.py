from uuid import UUID

from pydantic import BaseModel

from common.common_domain.valueobject.order_status import OrderStatus


class TrackOrderResponse(BaseModel, frozen=True):
    tracking_id: UUID
    status: OrderStatus
    failure_messages: list[str] | None