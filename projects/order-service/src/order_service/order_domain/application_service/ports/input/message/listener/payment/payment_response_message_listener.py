import typing as t

from order_service.order_domain.application_service.dto.message.payment_response import (
    PaymentResponse,
)


class PaymentResponseMessageListener(t.Protocol):
    def payment_completed(self, payment_response: PaymentResponse) -> None: ...

    def payment_cancelled(self, payment_response: PaymentResponse) -> None: ...
