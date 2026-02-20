from order_service.order_domain.application_service.dto.message.payment_response import PaymentResponse
from order_service.order_domain.application_service.ports.input.message.listener.payment.payment_response_message_listener import \
    PaymentResponseMessageListener


class PaymentResponseMessageListenerImpl(PaymentResponseMessageListener):

    def payment_completed(self, payment_response: PaymentResponse) -> None:
        ...

    def payment_cancelled(self, payment_response: PaymentResponse) -> None:
        ...