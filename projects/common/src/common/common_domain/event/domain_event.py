import abc
import typing as t

T = t.TypeVar("T")


class DomainEvent(abc.ABC, t.Generic[T]):
    pass
