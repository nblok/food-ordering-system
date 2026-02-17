from pydantic import BaseModel

from common.common_domain.valueobject.order_status import OrderStatus


class CreateOrderResponse(BaseModel, frozen=True):
    order_tracking_id: str
    status: OrderStatus
    message: str