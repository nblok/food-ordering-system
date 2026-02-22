from dependency_injector import containers, providers

from order_service.order_domain.application_service.ports.output.message.publisher import (
    OrderCreatedPaymentRequestMessagePublisher,
)


class Container(containers.DeclarativeContainer):
    providers.Factory(OrderCreatedPaymentRequestMessagePublisher)
