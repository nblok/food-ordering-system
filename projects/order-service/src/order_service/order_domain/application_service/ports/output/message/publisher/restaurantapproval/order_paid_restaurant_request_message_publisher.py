from common.common_domain.event.publisher.domain_event_publisher import (
    DomainEventPublisher,
)
from order_service.order_domain.domain_core.event.order_payed_event import (
    OrderPayedEvent,
)


class OrderPaidRestaurantRequestMessagePublisher(DomainEventPublisher[OrderPayedEvent]):
    pass
