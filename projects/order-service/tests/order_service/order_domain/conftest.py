import pytest

"""
TODO:
I don't think I need to use to di container here, since pytest has built-in
support for dependency injection. Just create a fixture for the interfaces
I want to be able to mock
"""

@pytest.fixture(scope="session")
def container():
    from order_service.order_application.container import Container
    order_service_container = Container()
    yield order_service_container

@pytest.fixture(scope="function")
def order_created_payment_request_message_publisher(mocker, container):
    yield container.reset_providers()