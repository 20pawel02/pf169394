import pytest

from src.CalculateDiscountedPrice import calculate_discounted_price


def test_discount_0_percent():
    assert calculate_discounted_price(10, 0) == 10


def test_discount_10_percent():
    assert calculate_discounted_price(100, 10) == 90


def test_discount_50_percent():
    assert calculate_discounted_price(50, 50) == 25


def test_discount_100_percent():
    assert calculate_discounted_price(100, 100) == 0


def test_discount_decimal():
    assert calculate_discounted_price(21, 3.7) == 20.22


def test_invalid_price_input():
    with pytest.raises(ValueError):
        calculate_discounted_price("100", 10)

def test():
    with pytest.raises(ValueError):
        calculate_discounted_price(-10, 10)

def test_invalid_discount_input():
    with pytest.raises(ValueError):
        calculate_discounted_price(100, "100")