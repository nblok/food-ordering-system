import typing as t

from order_service.order_domain.domain_core.entity.restaurant import Restaurant


class RestaurantRepository(t.Protocol):
    def find_restaurant_information(
        self, restaurant: Restaurant
    ) -> t.Optional[Restaurant]: ...
