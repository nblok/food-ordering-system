from enum import StrEnum


class OrderStatus(StrEnum):
    PENDING = "pending"
    PAID = "paid"
    APPROVED = "approved"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
