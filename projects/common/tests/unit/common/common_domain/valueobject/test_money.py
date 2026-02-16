from decimal import Decimal
from common.common_domain.valueobject.money import Money

def test_money_is_greater_than_zero_positive_amount():
    """Test that Money.is_greater_than_zero returns True for positive amounts."""
    money = Money(Decimal('100'))
    assert money.is_greater_than_zero() is True
    money = Money(Decimal('0.123'))

def test_money_is_greater_than_zero_zero_amount():
    """Test that Money.is_greater_than_zero returns False for 0."""
    money = Money(Decimal('0'))
    assert money.is_greater_than_zero() is False

def test_money_greater_than():
    fifty = Money(Decimal('50'))
    hundred = Money(Decimal('100'))
    assert (hundred > fifty) is True, f"Expected {hundred} > {fifty} to be True"
    assert (fifty > hundred) is False, f"Expected {fifty} > {hundred} to be False"
    assert (fifty > fifty)  is False, f"Expected {fifty} > {fifty} to be False"

def test_money_add():
    m1 = Money(Decimal('50.50'))
    m2 = Money(Decimal('100.25'))
    assert (m1 + m2) == Money(Decimal('150.75'))


