from abc import ABC, abstractmethod

from order_service.order_domain.domain_core.entity.order import Order
from order_service.order_domain.domain_core.entity.restaurant import Restaurant
from order_service.order_domain.domain_core.event.order_cancelled_event import OrderCancelledEvent
from order_service.order_domain.domain_core.event.order_created_event import OrderCreatedEvent
from order_service.order_domain.domain_core.event.order_payed_event import OrderPayedEvent


class OrderDomainService(ABC):

    @abstractmethod
    def validate_and_initiate_order(self, order: Order, restaurant: Restaurant) -> OrderCreatedEvent:
        ...

    @abstractmethod
    def pay_order(self, order: Order) -> OrderPayedEvent:
        ...

    @abstractmethod
    def approve_order(self, order: Order):
        ...

    @abstractmethod
    def cancel_order_payment(self, order: Order, failure_messages: list[str]) -> OrderCancelledEvent:
        ...

    @abstractmethod
    def cancel_order(self, order: Order, failure_messages: list[str]):
        ...