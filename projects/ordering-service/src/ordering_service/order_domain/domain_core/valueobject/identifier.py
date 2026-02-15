from dataclasses import dataclass
from common.common_domain.valueobject.identifier import Identifier
from uuid import UUID

@dataclass(frozen=True)
class OrderId(Identifier[UUID]):
    pass