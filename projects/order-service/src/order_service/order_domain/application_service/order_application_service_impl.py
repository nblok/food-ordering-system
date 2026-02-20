from order_service.order_domain.application_service.dto.create.create_order_command import CreateOrderCommand
from order_service.order_domain.application_service.dto.create.create_order_response import CreateOrderResponse
from order_service.order_domain.application_service.dto.track.track_order_query import TrackOrderQuery
from order_service.order_domain.application_service.dto.track.track_order_response import TrackOrderResponse
from order_service.order_domain.application_service.ports.input.service.order_application_service import \
    OrderApplicationService
from order_service.order_domain.application_service.order_create_command_handler import OrderCreateCommandHandler
from order_service.order_domain.application_service.order_track_command_handler import OrderTrackCommandHandler


class OrderApplicationServiceImpl(OrderApplicationService):
    """Implementation of OrderApplicationService interface/protocol for managing order-related operations."""
    def __init__(
        self,
        order_create_command_handler: OrderCreateCommandHandler,
        order_track_command_handler: OrderTrackCommandHandler,
    ):
        self._order_create_command_handler = order_create_command_handler
        self._order_track_command_handler = order_track_command_handler

    def create_order(self, create_order_command: CreateOrderCommand) -> CreateOrderResponse:
        return self._order_create_command_handler.create_order(create_order_command)

    def track_order(self, track_order_query: TrackOrderQuery) -> TrackOrderResponse:
        return self._order_track_command_handler.track_order(track_order_query)