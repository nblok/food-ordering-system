import typing as t
from dataclasses import dataclass

T = t.TypeVar("T")

@dataclass(frozen=True)
class Identifier(t.Generic[T]):
    value: T
