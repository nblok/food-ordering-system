import typing as t
from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_HALF_EVEN


@dataclass(frozen=True)
class Money:
    amount: Decimal

    @classmethod
    @property
    def zero(cls) -> t.Self:
        return cls(Decimal("0.00"))

    def is_greater_than_zero(self) -> bool:
        return self.amount > 0

    def __gt__(self, other: t.Self):
        return self.amount > other.amount

    def __add__(self, other: t.Self):
        return Money(self._set_scale(self.amount + other.amount))

    def __sub__(self, other: t.Self):
        return Money(self._set_scale(self.amount - other.amount))

    def __mul__(self, other: t.Self):
        return Money(self._set_scale(self.amount * other.amount))

    def multiply_by(self, multiplier: int):
        return Money(self._set_scale(self.amount * Decimal(f"{multiplier}")))

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return NotImplemented
        return self.amount == value.amount

    def __hash__(self) -> int:
        return hash(self.amount)

    def __str__(self):
        return f"{self.amount:.2f}"

    @classmethod
    def _set_scale(cls, value: Decimal) -> Decimal:
        with localcontext() as ctx:
            ctx.rounding = ROUND_HALF_EVEN
            return round(value, 2)

