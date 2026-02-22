from order_service.order_domain.application_service.dto.message.restaurant_approval_response import (
    RestaurantApprovalResponse,
)
from order_service.order_domain.application_service.ports.input.message.listener.restaurantapproval.restaurant_approval_response_message_listener import (
    RestaurantApprovalResponseMessageListener,
)


class RestaurantApprovalResponseMessageListenerImpl(
    RestaurantApprovalResponseMessageListener
):
    def order_approved(
        self, restaurant_approval_response: RestaurantApprovalResponse
    ) -> None: ...

    def order_rejected(
        self, restaurant_approval_response: RestaurantApprovalResponse
    ) -> None: ...
