from common.common_domain.entity.aggregateroot import AggregateRoot
from order_service.order_domain.domain_core.valueobject.identifier import OrderId


class Order(AggregateRoot[OrderId]):
    pass