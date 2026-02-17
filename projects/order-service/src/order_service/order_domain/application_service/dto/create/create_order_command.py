from decimal import Decimal
from pydantic import BaseModel
from uuid import UUID

from order_service.order_domain.application_service.dto.create.order_address import OrderAddress
from order_service.order_domain.application_service.dto.create.order_item import OrderItem


class CreateOrderCommand(BaseModel, frozen=True):
    customer_id: UUID
    restaurant_id: UUID
    price: Decimal
    items: list[OrderItem]
    address: OrderAddress