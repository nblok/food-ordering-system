import typing as t
import dataclasses
from common.common_domain.entity.aggregateroot import AggregateRoot
from common.common_domain.valueobject.identifier import OrderId, CustomerId, RestaurantId
from common.common_domain.valueobject.money import Money
from common.common_domain.valueobject.order_status import OrderStatus
from order_service.order_domain.domain_core.valueobject.street_address import (
    StreetAddress
)
from .order_item import OrderItem
from ..valueobject.identifier import TrackingId


class Order(AggregateRoot[OrderId]):
    def __init__(self, builder: "Order.Builder"):
        super().__init__(builder.order_id)
        self.customer_id = builder.customer_id
        self.restaurant_id = builder.restaurant_id
        self.street_address = builder.street_address
        self.price = builder.price
        self.items = builder.items
        self.tracking_id: t.Optional[TrackingId] = builder.tracking_id
        self.status: OrderStatus = (
            builder.status if builder.status else OrderStatus.PENDING
        )
        self.failure_messages: t.Optional[list[str]] = builder.failure_messages

    @classmethod
    def builder(cls) -> "Order.Builder":
        return cls.Builder()

    @dataclasses.dataclass(init=False)
    class Builder:
        order_id: OrderId
        customer_id: CustomerId
        restaurant_id: RestaurantId
        street_address: StreetAddress
        price: Money
        items: t.Sequence[OrderItem]
        tracking_id: t.Optional[TrackingId] = None
        status: t.Optional[OrderStatus] = None
        failure_messages: t.Optional[list[str]] = None

        def with_order_id(self, order_id: OrderId) -> "Order.Builder":
            self.order_id = order_id
            return self

        def with_customer_id(self, customer_id: CustomerId) -> "Order.Builder":
            self.customer_id = customer_id
            return self

        def with_restaurant_id(self, restaurant_id: RestaurantId) -> "Order.Builder":
            self.restaurant_id = restaurant_id
            return self

        def with_street_address(self, street_address: StreetAddress) -> "Order.Builder":
            self.street_address = street_address
            return self

        def with_price(self, price: Money) -> "Order.Builder":
            self.price = price
            return self

        def with_items(self, items: t.Sequence[OrderItem]) -> "Order.Builder":
            self.items = items
            return self

        def with_tracking_id(self, tracking_id: TrackingId) -> "Order.Builder":
            self.tracking_id = tracking_id
            return self

        def with_status(self, status: OrderStatus) -> "Order.Builder":
            self.status = status
            return self

        def with_failure_messages(self, failure_messages: list[str]) -> "Order.Builder":
            self.failure_messages = failure_messages
            return self

        def build(self) -> "Order":
            return Order(self)