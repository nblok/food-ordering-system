import logging
from order_service.order_domain.application_service.dto.track.track_order_query import TrackOrderQuery
from order_service.order_domain.application_service.dto.track.track_order_response import TrackOrderResponse
from order_service.order_domain.application_service.mapper.order_data_mapper import OrderDataMapper
from order_service.order_domain.application_service.ports.output.repository.order_repository import OrderRepository
from order_service.order_domain.domain_core.exception.order_not_found_exception import OrderNotFoundException
from order_service.order_domain.domain_core.valueobject.identifier import TrackingId


class OrderTrackCommandHandler:
    """Handler for processing order tracking commands."""

    def __init__(
        self,
        order_data_mapper: OrderDataMapper,
        order_repository: OrderRepository,
    ):
        self.order_data_mapper = order_data_mapper
        self.order_repository = order_repository

    def track_order(self, query: TrackOrderQuery) -> TrackOrderResponse:
        order = self.order_repository.find_by_tracking_id(TrackingId(query.tracking_id))
        if order is None:
            logging.warning(f"Order with tracking ID {query.tracking_id} not found")
            raise OrderNotFoundException(f"Order with tracking ID {query.tracking_id} not found")
        return self.order_data_mapper.order_to_track_order_response(order)