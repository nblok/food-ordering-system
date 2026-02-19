import typing as t


from order_service.order_domain.application_service.dto.message.restaurant_approval_response import \
    RestaurantApprovalResponse


class RestaurantApprovalResponseMessageListener(t.Protocol):

    def order_approved(self, restaurant_approval_response: RestaurantApprovalResponse) -> None:
        ...

    def order_rejected(self, restaurant_approval_response: RestaurantApprovalResponse) -> None:
        ...
