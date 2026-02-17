from enum import StrEnum


class OrderApprovalStatus(StrEnum):
    APPROVED = 'approved'
    REJECTED = 'rejected'