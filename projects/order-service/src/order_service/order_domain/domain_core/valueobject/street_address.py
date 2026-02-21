from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class StreetAddress:
    id: UUID
    street: str
    postal_code: str
    city: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StreetAddress):
            return False
        return (
            self.street == other.street
            and self.postal_code == other.postal_code
            and self.city == other.city
        )

    def __hash__(self) -> int:
        return hash((self.street, self.postal_code, self.city))
