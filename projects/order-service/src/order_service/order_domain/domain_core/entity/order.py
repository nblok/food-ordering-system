from common.common_domain.entity.aggregateroot import AggregateRoot
from common.common_domain.valueobject.identifier import OrderId


class Order(AggregateRoot[OrderId]):
    pass