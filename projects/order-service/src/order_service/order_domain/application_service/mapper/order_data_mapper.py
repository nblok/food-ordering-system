import logging
import uuid
from decimal import Decimal

from common.common_domain.valueobject.identifier import RestaurantId, ProductId, CustomerId, OrderId
from common.common_domain.valueobject.money import Money
from order_service.order_domain.application_service.dto.create.create_order_command import CreateOrderCommand
from order_service.order_domain.application_service.dto.create.create_order_response import CreateOrderResponse
from order_service.order_domain.application_service.dto.create.order_address import OrderAddress
from order_service.order_domain.application_service.dto.create.order_item import OrderItem as OrderItemDTO
from order_service.order_domain.domain_core.entity.order import Order
from order_service.order_domain.domain_core.entity.order_item import OrderItem
from order_service.order_domain.domain_core.entity.product import Product
from order_service.order_domain.domain_core.entity.restaurant import Restaurant
from order_service.order_domain.domain_core.exception.order_domain_exception import OrderDomainException
from order_service.order_domain.domain_core.valueobject.street_address import StreetAddress


class OrderDataMapper:

    def create_order_command_to_restaurant(self, command: CreateOrderCommand) -> Restaurant:
        restaurant = self.restaurant_repository.find_restaurant(command.restaurant_id)
        if not restaurant:
            logging.warning(f'could not find restaurant {command.restaurant_id}')
            raise OrderDomainException(f'could not find restaurant {command.restaurant_id}')
        return (
            restaurant.builder()
                .restaurant_id(RestaurantId(command.restaurant_id))
                .products(map(
                    lambda item: Product(ProductId(item.product_id)),
                    command.items
                ))
                .build()
        )

    def create_order_command_to_order(self, command: CreateOrderCommand) -> Order:
        return (
            Order.builder()
                .with_customer_id(CustomerId(command.customer_id))
                .with_restaurant_id(RestaurantId(command.restaurant_id))
                .with_street_address(self.order_address_to_street_address(
                    command.address
                ))
                .with_price(Money(command.price))
                .with_items(self.order_items_to_order_item_entities(command.items))
                .build()
        )

    def order_to_create_order_response(self, order: Order, message: str) -> CreateOrderResponse:
        return CreateOrderResponse.model_validate(dict(
            order_tracking_id=order.tracking_id,
            status=order.status,
            message=message
        ))

    def order_items_to_order_item_entities(self, items: list[OrderItemDTO]) -> list[OrderItem]:
        return list(map(
            lambda item: (
                OrderItem.builder()
                    .with_product(Product(ProductId(item.product_id)))
                    .with_price(Money(item.price))
                    .with_quantity(item.quantity)
                    .with_sub_total(Money(item.sub_total))
                    .build()
            ),
            items
        ))

    def order_address_to_street_address(self, address: OrderAddress) -> StreetAddress:
        return StreetAddress(
            uuid.uuid4(),
            address.street,
            address.postal_code,
            address.city
        )