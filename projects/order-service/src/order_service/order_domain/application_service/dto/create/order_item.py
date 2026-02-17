from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class OrderItem(BaseModel, frozen=True):
    product_id: UUID
    quantity: int
    price: Decimal
    sub_total: Decimal