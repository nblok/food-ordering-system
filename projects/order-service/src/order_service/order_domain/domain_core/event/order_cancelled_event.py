import datetime
from common.common_domain.event.domain_event import DomainEvent

from ..entity.order import Order


class OrderCancelledEvent(DomainEvent[Order]):

    def __init__(self, order: Order, created_at: datetime.datetime):
        self.order = order
        self.created_at = created_at
