from pydantic import BaseModel, ConfigDict
from uuid import UUID
from decimal import Decimal


class OrderItem(BaseModel):
    model_config = ConfigDict(frozen=True)
    product_id: UUID
    quantity: int
    price: Decimal
    sub_total: Decimal
