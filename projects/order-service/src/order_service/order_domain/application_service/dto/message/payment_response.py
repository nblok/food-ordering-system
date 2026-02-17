import datetime

from pydantic import BaseModel, ConfigDict
from decimal import Decimal

from common.common_domain.valueobject.payment_status import PaymentStatus


class PaymentResponse(BaseModel):
    model_config = ConfigDict(frozen=True)
    id: str
    saga_id: str
    order_id: str
    payment_id: str
    customer_id: str
    price: Decimal
    created_at: datetime.datetime
    payment_status: PaymentStatus
    failure_messages: list[str] | None