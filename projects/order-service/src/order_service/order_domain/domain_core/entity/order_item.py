import typing as t
import dataclasses
from common.common_domain.entity.baseentity import BaseEntity
from common.common_domain.valueobject.money import Money
from order_service.order_domain.domain_core.valueobject.identifier import OrderItemId
from order_service.order_domain.domain_core.entity.product import Product


class OrderItem(BaseEntity[OrderItemId]):
    def __init__(self, builder: "OrderItem.Builder"):
        super().__init__(builder.order_item_id)
        self.product_id = builder.product
        self.quantity = builder.quantity
        self.price = builder.price
        self.sub_total = builder.sub_total

    @classmethod
    def builder(cls) -> "OrderItem.Builder":
        return cls.Builder()

    @dataclasses.dataclass(init=False)
    class Builder:
        order_item_id: OrderItemId
        product: Product
        quantity: int
        price: Money
        sub_total: Money

        def with_order_item_id(self, order_item_id: OrderItemId) -> t.Self:
            self.order_item_id = order_item_id
            return self

        def with_product(self, product: Product) -> t.Self:
            self.product = product
            return self

        def with_quantity(self, quantity: int) -> t.Self:
            self.quantity = quantity
            return self

        def with_price(self, price: Money) -> t.Self:
            self.price = price
            return self

        def with_sub_total(self, sub_total: Money) -> t.Self:
            self.sub_total = sub_total
            return self

        def build(self) -> 'OrderItem':
            return OrderItem(self)
