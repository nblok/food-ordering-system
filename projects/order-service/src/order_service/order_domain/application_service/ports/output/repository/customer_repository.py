import typing as t
from uuid import UUID

from order_service.order_domain.domain_core.entity.customer import Customer


class CustomerRepository(t.Protocol):
    def find_customer(self, customer_id: UUID) -> t.Optional[Customer]: ...
