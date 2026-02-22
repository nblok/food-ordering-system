import logging

from order_service.order_domain.application_service.dto.create.create_order_command import (
    CreateOrderCommand,
)
from order_service.order_domain.application_service.dto.create.create_order_response import (
    CreateOrderResponse,
)
from order_service.order_domain.application_service.mapper.order_data_mapper import (
    OrderDataMapper,
)
from order_service.order_domain.application_service.order_create_helper import (
    OrderCreateHelper,
)
from order_service.order_domain.application_service.ports.output.message.publisher.payment.order_created_payment_request_message_publisher import (
    OrderCreatedPaymentRequestMessagePublisher,
)


class OrderCreateCommandHandler:
    """Handler for processing order creation commands."""

    def __init__(
        self,
        order_create_helper: OrderCreateHelper,
        order_data_mapper: OrderDataMapper,
        order_created_payment_request_message_publisher: OrderCreatedPaymentRequestMessagePublisher,
    ):
        self.order_create_helper = order_create_helper
        self.order_data_mapper = order_data_mapper
        self.order_created_payment_request_message_publisher = (
            order_created_payment_request_message_publisher
        )

    def create_order(self, command: CreateOrderCommand) -> CreateOrderResponse:
        order_created_event = self.order_create_helper.persist_order(command)
        logging.info(f"Order created with id {order_created_event.order.id}")
        self.order_created_payment_request_message_publisher.publish(
            order_created_event
        )
        return self.order_data_mapper.order_to_create_order_response(
            order_created_event.order, "Order created successfully"
        )
