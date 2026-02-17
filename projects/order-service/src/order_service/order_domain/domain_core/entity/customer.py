from common.common_domain.entity.aggregateroot import AggregateRoot
from common.common_domain.valueobject.identifier import CustomerId


class Customer(AggregateRoot[CustomerId]):
    pass
