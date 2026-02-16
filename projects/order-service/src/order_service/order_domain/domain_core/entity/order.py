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
        self._trackingId: t.Optional[TrackingId] = builder._tracking_id
        self._status: OrderStatus = (
            builder._status if builder._status else OrderStatus.PENDING
        )
        self._failure_messages: t.Optional[list[str]] = builder._failure_messages

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
        _tracking_id: t.Optional[TrackingId]
        _status: t.Optional[OrderStatus]
        _failure_messages: t.Optional[list[str]]

        def order_id(self, order_id: OrderId) -> t.Self:
            self.order_id = order_id
            return self

        def customer_id(self, customer_id: CustomerId) -> t.Self:
            self.customer_id = customer_id
            return self

        def restaurant_id(self, restaurant_id: RestaurantId) -> t.Self:
            self.restaurant_id = restaurant_id
            return self

        def street_address(self, street_address: StreetAddress) -> t.Self:
            self.street_address = street_address
            return self

        def price(self, price: Money) -> t.Self:
            self.price = price
            return self

        def items(self, items: t.Sequence[OrderItem]) -> t.Self:
            self.items = items
            return self

        def tracking_id(self, tracking_id: TrackingId) -> t.Self:
            self._tracking_id = tracking_id
            return self

        def status(self, status: OrderStatus) -> t.Self:
            self._status = status
            return self

        def failure_messages(self, failure_messages: list[str]) -> t.Self:
            self._failure_messages = failure_messages
            return self

        def build(self) -> "Order":
            return Order(self)