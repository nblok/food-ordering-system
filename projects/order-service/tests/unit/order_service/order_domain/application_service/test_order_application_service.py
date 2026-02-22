import decimal
import pytest
import uuid

from common.common_domain.exception.domain_exception import DomainException
from common.common_domain.valueobject.order_status import OrderStatus
from order_service.order_domain.domain_core.entity.customer import Customer
from order_service.order_domain.domain_core.entity.product import Product
from order_service.order_domain.domain_core.entity.restaurant import Restaurant
from common.common_domain.valueobject.money import Money
from common.common_domain.valueobject.identifier import CustomerId, RestaurantId, ProductId, OrderId
from order_service.order_domain.application_service.dto.create.create_order_command import CreateOrderCommand
from order_service.order_domain.application_service.dto.create.order_address import OrderAddress
from order_service.order_domain.application_service.dto.create.order_item import OrderItem
from order_service.order_domain.domain_core.exception.order_domain_exception import OrderDomainException


class TestOrderApplicationService:
    CUSTOMER_ID = uuid.UUID('123e4567-e89b-12d3-a456-426614174000')
    RESTAURANT_ID = uuid.UUID('123e4567-e89b-12d3-a456-426614174001')
    PRODUCT_ID = uuid.UUID('123e4567-e89b-12d3-a456-426614174003')
    ORDER_ID = uuid.UUID('123e4567-e89b-12d3-a456-426614174002')
    PRICE = decimal.Decimal('200.00')


    @pytest.fixture(autouse=True)
    def setup(
        self,
        order_application_service,
        order_data_mapper,
        customer_repository,
        restaurant_repository,
        order_repository,
    ):
        self.order_application_service = order_application_service
        self.create_order_command = CreateOrderCommand(
            customer_id=self.CUSTOMER_ID,
            restaurant_id=self.RESTAURANT_ID,
            address=OrderAddress(
                city='test city',
                street='test street address',
                postal_code='123456',
            ),
            price=self.PRICE,
            items=[
                OrderItem(
                    product_id=self.PRODUCT_ID,
                    quantity=1,
                    price=decimal.Decimal('50.00'),
                    sub_total=decimal.Decimal('50.00')
                ),
                OrderItem(
                    product_id=self.PRODUCT_ID,
                    quantity=3,
                    price=decimal.Decimal('50.00'),
                    sub_total=decimal.Decimal('150.00')
                )
            ]
        )
        self.create_order_command_wrong_total_price = CreateOrderCommand(
            customer_id=self.CUSTOMER_ID,
            restaurant_id=self.RESTAURANT_ID,
            address=OrderAddress(
                city='Paris',
                street='street 1',
                postal_code='1000AB',
            ),
            price=decimal.Decimal('250.00'),
            items=[
                OrderItem(
                    product_id=self.PRODUCT_ID,
                    quantity=1,
                    price=decimal.Decimal('50.00'),
                    sub_total=decimal.Decimal('50.00')
                ),
                OrderItem(
                    product_id=self.PRODUCT_ID,
                    quantity=3,
                    price=decimal.Decimal('50.00'),
                    sub_total=decimal.Decimal('150.00')
                )
            ]
        )
        self.create_order_command_wrong_product_price = CreateOrderCommand(
            customer_id=self.CUSTOMER_ID,
            restaurant_id=self.RESTAURANT_ID,
            address=OrderAddress(
                city='Paris',
                street='street 1',
                postal_code='1000AB',
            ),
            price=decimal.Decimal('210.00'),
            items=[
                OrderItem(
                    product_id=self.PRODUCT_ID,
                    quantity=1,
                    price=decimal.Decimal('60.00'),
                    sub_total=decimal.Decimal('60.00')
                ),
                OrderItem(
                    product_id=self.PRODUCT_ID,
                    quantity=3,
                    price=decimal.Decimal('50.00'),
                    sub_total=decimal.Decimal('150.00')
                )
            ]
        )
        self.customer = Customer(CustomerId(self.CUSTOMER_ID))
        self.restaurant_response = (Restaurant.builder()
            .with_restaurant_id(RestaurantId(self.RESTAURANT_ID))
            .with_products([
                Product(ProductId(self.PRODUCT_ID), 'product-1', Money(decimal.Decimal('50.00'))),
                Product(ProductId(self.PRODUCT_ID), 'product-2', Money(decimal.Decimal('50.00')))
            ])
            .with_active(True)
            .build()
        )
        self.order = order_data_mapper.create_order_command_to_order(self.create_order_command)
        self.order.id = OrderId(self.ORDER_ID)
        customer_repository.find_customer.return_value = self.customer
        restaurant_repository.find_restaurant_information.return_value = self.restaurant_response
        order_repository.save.return_value = self.order

    def test_create_order(self):
        response = self.order_application_service.create_order(self.create_order_command)
        assert response.status == OrderStatus.PENDING
        assert response.message == 'Order created successfully'
        assert response.order_tracking_id is not None

    def test_create_order_wrong_total_price(self):
        with pytest.raises(OrderDomainException) as excinfo:
            self.order_application_service.create_order(
                self.create_order_command_wrong_total_price
            )
        assert str(excinfo.value) == \
               f'Order items total price 200.00 does not match order total price 250.00.'

    def test_create_order_wrong_product_price(self):
        with pytest.raises(OrderDomainException) as excinfo:
            self.order_application_service.create_order(
                self.create_order_command_wrong_product_price
            )
        assert str(excinfo.value) == \
            f'Order item price is invalid 60.00 for product {self.PRODUCT_ID}.'

    def test_create_order_with_passive_restaurant(self, restaurant_repository):
        passive_restaurant = (
            Restaurant.builder()
                .with_restaurant_id(RestaurantId(self.RESTAURANT_ID))
                .with_products([
                   Product(ProductId(self.PRODUCT_ID), 'product-1', Money(decimal.Decimal('50.00'))),
                   Product(ProductId(self.PRODUCT_ID), 'product-2', Money(decimal.Decimal('50.00')))
                ])
                .with_active(False)
                .build()
        )
        restaurant_repository.find_restaurant_information.return_value = passive_restaurant
        with pytest.raises(OrderDomainException) as excinfo:
            self.order_application_service.create_order(self.create_order_command)
        assert str(excinfo.value) == f'Restaurant {self.RESTAURANT_ID} is not active.'
