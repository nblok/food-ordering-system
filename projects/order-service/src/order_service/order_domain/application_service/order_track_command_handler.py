from order_service.order_domain.application_service.dto.track.track_order_query import TrackOrderQuery
from order_service.order_domain.application_service.dto.track.track_order_response import TrackOrderResponse


class OrderTrackCommandHandler:
    """Handler for processing order tracking commands."""

    def track_order(self, query: TrackOrderQuery) -> TrackOrderResponse:
        ...