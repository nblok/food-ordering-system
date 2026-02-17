import typing as t
import dataclasses
import uuid
import functools
import operator

from common.common_domain.entity.aggregateroot import AggregateRoot
from common.common_domain.valueobject.identifier import OrderId, CustomerId, RestaurantId
from common.common_domain.valueobject.money import Money
from common.common_domain.valueobject.order_status import OrderStatus
from order_service.order_domain.domain_core.valueobject.street_address import (
    StreetAddress
)
from .order_item import OrderItem
from ..valueobject.identifier import TrackingId, OrderItemId
from ..exception.order_domain_exception import OrderDomainException


class Order(AggregateRoot[OrderId]):
    def __init__(self, builder: "Order.Builder"):
        super().__init__(builder.order_id)
        self.customer_id = builder.customer_id
        self.restaurant_id = builder.restaurant_id
        self.street_address = builder.street_address
        self.price = builder.price
        self.items = builder.items
        self.tracking_id: t.Optional[TrackingId] = builder.tracking_id
        self.status: t.Optional[OrderStatus] = builder.status
        self.failure_messages: t.Optional[list[str]] = builder.failure_messages

    def initialize_order(self):
        self.id = OrderId(uuid.uuid4())
        self.tracking_id = TrackingId(uuid.uuid4())
        self.status = OrderStatus.PENDING
        self._initialize_order_items()

    def validate_order(self):
        self._validate_initial_order()
        self._validate_total_price()
        self._validate_items_price()

    def pay(self):
        if self.status is not OrderStatus.PENDING:
            raise OrderDomainException("Order cannot be paid if it is not in pending status.")
        self.status = OrderStatus.PAID

    def approve(self):
        if self.status is not OrderStatus.PAID:
            raise OrderDomainException("Order cannot be approved if it is not in paid status.")
        self.status = OrderStatus.APPROVED

    def init_cancel(self, failure_messages: list[str]):
        if self.status is not OrderStatus.PAID:
            raise OrderDomainException("Order cannot be canceled if it is not in paid status.")
        self.status = OrderStatus.CANCELLING
        self.update_failure_messages(failure_messages)

    def cancel(self, failure_messages: list[str]):
        if self.status not in {OrderStatus.CANCELLING, OrderStatus.PENDING}:
            raise OrderDomainException("Order cannot be canceled if it is not in cancelling or pending status.")
        self.status = OrderStatus.CANCELLED
        self.update_failure_messages(failure_messages)

    def update_failure_messages(self, failure_messages: list[str]):
        if self.failure_messages is not None:
            self.failure_messages.extend(failure_messages)
        else:
            self.failure_messages = failure_messages

    def _initialize_order_items(self):
        item_id = 1
        for order_item in self.items:
            order_item.initialize_order_item(t.cast(OrderId, self.id), OrderItemId(item_id))

    def _validate_initial_order(self):
        if self.status is not None or self.id is not None:
            raise OrderDomainException("Order cannot be initialized with existing status or id.")

    def _validate_total_price(self):
        if not self.price.is_greater_than_zero():
            raise OrderDomainException("Order total price cannot be zero or negative.")

    def _validate_items_price(self):
        def validate_item_and_return_sub_total(order_item: OrderItem):
            self._validate_item_price(order_item)
            return order_item.sub_total
        order_items_total = functools.reduce(
            operator.add, map(validate_item_and_return_sub_total, self.items), Money.zero
        )
        if not self.price == order_items_total:
            raise OrderDomainException("Order items total price does not match order total price.")

    @staticmethod
    def _validate_item_price(order_item: OrderItem):
        if not order_item.is_price_valid():
            raise OrderDomainException("Order item price is invalid.")

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