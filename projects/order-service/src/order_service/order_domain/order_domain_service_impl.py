import logging as log

from common.common_lib.zoned_datetime import ZonedDateTime
from order_service.order_domain.domain_core.entity.order import Order
from order_service.order_domain.domain_core.entity.restaurant import Restaurant
from order_service.order_domain.domain_core.event.order_cancelled_event import OrderCancelledEvent
from order_service.order_domain.domain_core.event.order_created_event import OrderCreatedEvent
from order_service.order_domain.domain_core.event.order_payed_event import OrderPayedEvent
from order_service.order_domain.domain_core.exception.order_domain_exception import OrderDomainException
from order_service.order_domain.order_domain_service import OrderDomainService


class OrderDomainServiceImpl(OrderDomainService):
    def validate_and_initiate_order(self, order: Order, restaurant: Restaurant) -> OrderCreatedEvent:
        self._validate_restaurant(restaurant)
        self._set_order_product_information(order, restaurant)
        order.validate_order()
        order.initialize_order()
        log.info(f"Order {order.id} created successfully.")
        return OrderCreatedEvent(order, ZonedDateTime.utc_now())

    def pay_order(self, order: Order) -> OrderPayedEvent:
        order.pay()
        log.info(f"Order {order.id} payment processed successfully.")
        return OrderPayedEvent(order, ZonedDateTime.utc_now())

    def approve_order(self, order: Order):
        order.approve()
        log.info(f"Order {order.id} approved successfully.")

    def cancel_order_payment(self, order: Order, failure_messages: list[str]) -> OrderCancelledEvent:
        order.init_cancel(failure_messages)
        return OrderCancelledEvent(order, ZonedDateTime.utc_now())

    def cancel_order(self, order: Order, failure_messages: list[str]):
        order.cancel(failure_messages)
        log.info(f"Order {order.id} canceled successfully.")

    def _validate_restaurant(self, restaurant: Restaurant):
        if not restaurant.active:
            raise OrderDomainException(f"Restaurant is {restaurant.id} not active.")

    def _set_order_product_information(self, order: Order, restaurant: Restaurant):
        # TODO: optimize this, use dict instead of loops
        for order_item in order.items:
            for restaurant_product in restaurant.products:
                current_product = order_item.product
                if current_product == restaurant_product:
                    current_product.update_with_confirmed_name_and_price(
                        restaurant_product.name, restaurant_product.price
                    )
