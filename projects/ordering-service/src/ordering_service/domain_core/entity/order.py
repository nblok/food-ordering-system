from common.common_domain.entity.aggregateroot import AggregateRoot
from ordering_service.domain_core.valueobject.identifier import OrderId


class Order(AggregateRoot[OrderId]):
    pass