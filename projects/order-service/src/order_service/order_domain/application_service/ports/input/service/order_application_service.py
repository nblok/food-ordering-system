import typing as t

from order_service.order_domain.application_service.dto.create.create_order_command import CreateOrderCommand
from order_service.order_domain.application_service.dto.create.create_order_response import CreateOrderResponse
from order_service.order_domain.application_service.dto.track.track_order_query import TrackOrderQuery
from order_service.order_domain.application_service.dto.track.track_order_response import TrackOrderResponse


class OrderApplicationService(t.Protocol):

    def create_order(self, create_order_command: CreateOrderCommand) -> CreateOrderResponse: ...

    def track_order(self, track_order_query: TrackOrderQuery) -> TrackOrderResponse: ...