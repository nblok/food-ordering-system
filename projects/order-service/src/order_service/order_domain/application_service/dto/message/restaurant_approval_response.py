import datetime

from pydantic import BaseModel

from common.common_domain.valueobject.order_approval_status import OrderApprovalStatus


class RestaurantApprovalResponse(BaseModel, frozen=True):
    id: str
    saga_id: str
    order_id: str
    restaurant_id: str
    created_at: datetime.datetime
    order_approval_status: OrderApprovalStatus
    failure_messages: list[str] | None