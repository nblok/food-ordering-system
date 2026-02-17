import uuid
import decimal

from common.common_domain.valueobject.money import Money
from common.common_domain.valueobject.identifier import (
    OrderId,
    CustomerId,
    RestaurantId,
    ProductId
)
from order_service.order_domain.domain_core.entity.order import Order
from order_service.order_domain.domain_core.entity.product import Product
from order_service.order_domain.domain_core.entity.order_item import OrderItem
from order_service.order_domain.domain_core.valueobject.identifier import OrderItemId
from order_service.order_domain.domain_core.valueobject.street_address import (
    StreetAddress
)


def test_order_id():
    order_id = OrderId(uuid.uuid4())
    order = (
        Order.builder()
            .with_order_id(order_id)
            .with_customer_id(CustomerId(uuid.uuid4()))
            .with_restaurant_id(RestaurantId(uuid.uuid4()))
            .with_street_address(
                StreetAddress(
                    id=uuid.uuid4(),
                    street='123 Main St',
                    postal_code=12345,
                    city='Anytown'
                )
            )
            .with_price(Money(decimal.Decimal('100.38')))
            .with_items([
                OrderItem.builder()
                    .with_order_item_id(OrderItemId(1))
                    .with_order_id(order_id)
                    .with_product(
                        Product(
                            ProductId(uuid.uuid4()),
                            name='Test Product',
                            price=Money(decimal.Decimal('100.38'))
                        )
                    )
                    .with_quantity(1)
                    .with_price(Money(decimal.Decimal('100.38')))
                    .with_sub_total(Money(decimal.Decimal('100.38')))
                    .build()
            ])
            .build()
    )
    assert order_id == order.id
