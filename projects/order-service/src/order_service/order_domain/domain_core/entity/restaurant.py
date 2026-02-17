import typing as t
import dataclasses

from common.common_domain.entity.aggregateroot import AggregateRoot
from common.common_domain.valueobject.identifier import RestaurantId

from .product import Product


class Restaurant(AggregateRoot[RestaurantId]):
    def __init__(self, builder: "Restaurant.Builder"):
        super().__init__(builder.restaurant_id)
        self.products: list[Product] = builder.products
        self.active: bool = builder.active

    @classmethod
    def builder(cls) -> "Restaurant.Builder":
        return cls.Builder()

    @dataclasses.dataclass(init=False)
    class Builder:
        restaurant_id: RestaurantId
        products: list[Product]
        active: bool

        def with_restaurant_id(
            self, restaurant_id: RestaurantId
        ) -> "Restaurant.Builder":
            self.restaurant_id = restaurant_id
            return self

        def with_products(self, products: list[Product]) -> "Restaurant.Builder":
            self.products = products
            return self

        def with_active(self, active: bool) -> "Restaurant.Builder":
            self.active = active
            return self

        def build(self) -> "Restaurant":
            return Restaurant(self)
