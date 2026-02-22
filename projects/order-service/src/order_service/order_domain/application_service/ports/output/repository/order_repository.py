import typing as t

from order_service.order_domain.domain_core.entity.order import Order
from order_service.order_domain.domain_core.valueobject.identifier import TrackingId


class OrderRepository(t.Protocol):
    def save(self, order: Order) -> Order: ...

    def find_by_tracking_id(self, tracking_id: TrackingId) -> t.Optional[Order]: ...
