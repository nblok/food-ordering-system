from pydantic import BaseModel, ConfigDict

from common.common_domain.valueobject.order_status import OrderStatus


class CreateOrderResponse(BaseModel):
    model_config = ConfigDict(frozen=True)
    order_tracking_id: str
    status: OrderStatus
    message: str
