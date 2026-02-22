from uuid import UUID

from common.common_domain.valueobject.identifier import Identifier


class OrderItemId(Identifier[int]):
    pass


class TrackingId(Identifier[UUID]):
    pass
