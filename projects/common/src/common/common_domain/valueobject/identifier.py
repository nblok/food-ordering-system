import typing as t
from dataclasses import dataclass
from uuid import UUID

T = t.TypeVar("T")


@dataclass(frozen=True)
class Identifier(t.Generic[T]):
    value: T


@dataclass(frozen=True)
class OrderId(Identifier[UUID]):
    pass


@dataclass(frozen=True)
class ProductId(Identifier[UUID]):
    pass


@dataclass(frozen=True)
class RestaurantId(Identifier[UUID]):
    pass


@dataclass(frozen=True)
class CustomerId(Identifier[UUID]):
    pass
