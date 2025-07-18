from app import calculate_quote


def test_positive_markup():
    assert calculate_quote(100, 20) == 120


def test_negative_markup():
    assert calculate_quote(100, -50) == 50


def test_zero_markup():
    assert calculate_quote(200, 0) == 200


def test_invalid_inputs():
    import pytest
    with pytest.raises(ValueError):
        calculate_quote(-10, 10)
    with pytest.raises(ValueError):
        calculate_quote(100, -150)
