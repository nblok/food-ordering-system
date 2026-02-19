import logging
from uuid import UUID

from order_service.order_domain.application_service.dto.create.create_order_command import CreateOrderCommand
from order_service.order_domain.application_service.dto.create.create_order_response import CreateOrderResponse
from order_service.order_domain.application_service.mapper.order_data_mapper import OrderDataMapper
from order_service.order_domain.application_service.ports.output.repository.customer_repository import \
    CustomerRepository
from order_service.order_domain.application_service.ports.output.repository.order_repository import OrderRepository
from order_service.order_domain.application_service.ports.output.repository.restaurant_repository import \
    RestaurantRepository
from order_service.order_domain.domain_core.exception.order_domain_exception import OrderDomainException
from order_service.order_domain.order_domain_service import OrderDomainService


class OrderCreateCommandHandler:
    """Handler for processing order creation commands."""
    def __init__(
        self,
        order_domain_service: OrderDomainService,
        order_repository: OrderRepository,
        customer_repository: CustomerRepository,
        restaurant_repository: RestaurantRepository,
        order_data_mapper: OrderDataMapper
    ):
        self.order_domain_service = order_domain_service
        self.order_repository = order_repository
        self.customer_repository = customer_repository
        self.restaurant_repository = restaurant_repository
        self.order_data_mapper = order_data_mapper

    # TODO: make this method transactional
    def create_order(self, command: CreateOrderCommand) -> CreateOrderResponse:
        self.check_customer(command.customer_id)
        restaurant = self.check_restaurant(command)
        order = self.order_data_mapper.create_order_command_to_order(command)
        order_created_event = self.order_domain_service.validate_and_initiate_order(order, restaurant)
        persisted_order = self.save_order(order)
        return self.order_data_mapper.order_to_create_order_response(
            persisted_order, 'Order created successfully'
        )



    def check_restaurant(self, command: CreateOrderCommand):
        restaurant = self.order_data_mapper.create_order_command_to_restaurant(command)
        optionalRestaurant = self.restaurant_repository.find_restaurant_information(restaurant)
        if not optionalRestaurant:
            logging.warning(f'could not find restaurant {command.restaurant_id}')
            raise OrderDomainException(f'could not find restaurant {command.restaurant_id}')
        return optionalRestaurant

    def check_customer(self, customer_id: UUID):
        customer = self.customer_repository.find_customer(customer_id)
        if not customer:
            logging.warning(f'could not find customer {customer_id}')
            raise OrderDomainException(f'could not find customer {customer_id}')

    def save_order(self, order):
        result = self.order_repository.save(order)
        if not result:
            logging.warning('Failed to save order')
            raise OrderDomainException('Failed to save order')
        logging.info(f'Saved order with id {order.id}')
        return result
