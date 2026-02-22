import typing as t
# from abc import ABC

ID = t.TypeVar("ID")


class BaseEntity(t.Generic[ID]):
    def __init__(self, identifier: ID | None):
        self._id = identifier

    @property
    def id(self) -> ID | None:
        return self._id

    @id.setter
    def id(self, value: ID | None):
        self._id = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(identifier={self.id})"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return NotImplemented
        return self.id == value.id

    def __hash__(self) -> int:
        return hash(self.id)
