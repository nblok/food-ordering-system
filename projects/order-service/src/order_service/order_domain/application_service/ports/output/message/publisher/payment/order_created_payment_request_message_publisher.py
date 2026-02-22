from uuid import UUID

from common.common_domain.event.publisher.domain_event_publisher import (
    DomainEventPublisher,
)
from order_service.order_domain.domain_core.event.order_created_event import (
    OrderCreatedEvent,
)


class OrderCreatedPaymentRequestMessagePublisher(
    DomainEventPublisher[OrderCreatedEvent]
):
    pass
