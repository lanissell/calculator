import pytest
from BankCalculator import BankCalculator as bc


def test_calculate_monthly_payment_regular_case():
    """Тестируем расчет для обычных данных"""
    result = bc.calculate_monthly_payment(100000, 5, 20)
    assert result == pytest.approx(6, rel=1e-2)


def test_calculate_monthly_payment_zero_interest():
    """Тест для ставки 0%"""
    result = bc.calculate_monthly_payment(120000, 0, 20)
    assert result == 120000 / (20 * 12)


def test_calculate_monthly_payment_large_loan():
    """Тест для большого кредита"""
    result = bc.calculate_monthly_payment(10000000, 7, 30)
    assert result == pytest.approx(66530.249, rel=1e-2)


def test_calculate_monthly_payment_small_loan():
    """Тест для маленького кредита"""
    result = bc.calculate_monthly_payment(1000, 5, 1)
    assert result == pytest.approx(85.71, rel=1e-2)