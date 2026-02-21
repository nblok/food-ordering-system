import pytest

from order_service.order_domain.application_service.order_track_command_handler import OrderTrackCommandHandler
from order_service.order_domain.application_service.order_create_helper import OrderCreateHelper
from order_service.order_domain.application_service.order_create_command_handler import OrderCreateCommandHandler
from order_service.order_domain.application_service.mapper.order_data_mapper import OrderDataMapper
from order_service.order_domain.application_service.order_application_service_impl import OrderApplicationServiceImpl
from order_service.order_domain.order_domain_service_impl import OrderDomainServiceImpl
from order_service.order_domain.application_service.ports.output.repository.customer_repository import \
    CustomerRepository
from order_service.order_domain.application_service.ports.output.repository.order_repository import OrderRepository
from order_service.order_domain.application_service.ports.output.message.publisher import \
    OrderCreatedPaymentRequestMessagePublisher, OrderCancelledPaymentRequestMessagePublisher
from order_service.order_domain.application_service.ports.output.message.publisher import \
    OrderPaidRestaurantRequestMessagePublisher
from order_service.order_domain.application_service.ports.output.repository.restaurant_repository import \
    RestaurantRepository


@pytest.fixture(scope="function")
def order_created_payment_request_message_publisher(mocker):
    yield mocker.Mock(spec=OrderCreatedPaymentRequestMessagePublisher)


@pytest.fixture(scope="function")
def order_cancelled_payment_request_message_publisher(mocker):
    yield mocker.Mock(spec=OrderCancelledPaymentRequestMessagePublisher)


@pytest.fixture(scope="function")
def order_paid_restaurant_request_message_publisher(mocker):
    yield mocker.Mock(spec=OrderPaidRestaurantRequestMessagePublisher)


@pytest.fixture(scope="function")
def order_repository(mocker):
    yield mocker.Mock(spec=OrderRepository)


@pytest.fixture(scope="function")
def customer_repository(mocker):
    yield mocker.Mock(spec=CustomerRepository)


@pytest.fixture(scope="function")
def restaurant_repository(mocker):
    yield mocker.Mock(spec=RestaurantRepository)


@pytest.fixture(scope="function")
def order_domain_service():
    yield OrderDomainServiceImpl()


@pytest.fixture(scope="function")
def order_data_mapper():
    yield OrderDataMapper()

@pytest.fixture(scope="function")
def order_create_helper(
    order_domain_service,
    order_repository,
    customer_repository,
    restaurant_repository,
    order_data_mapper
):
    yield OrderCreateHelper(
        order_domain_service,
        order_repository,
        customer_repository,
        restaurant_repository,
        order_data_mapper
    )

@pytest.fixture(scope="function")
def order_create_command_handler(
    order_create_helper,
    order_data_mapper,
    order_created_payment_request_message_publisher
):
    yield OrderCreateCommandHandler(
        order_create_helper,
        order_data_mapper,
        order_created_payment_request_message_publisher
    )


@pytest.fixture(scope="function")
def order_track_command_handler(order_data_mapper, order_repository):
    yield OrderTrackCommandHandler(order_data_mapper, order_repository)


@pytest.fixture(scope="function")
def order_application_service(order_create_command_handler, order_track_command_handler):
    yield OrderApplicationServiceImpl(
        order_create_command_handler, order_track_command_handler
    )




