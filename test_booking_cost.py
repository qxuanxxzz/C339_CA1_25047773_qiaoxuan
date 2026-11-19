import pytest
from booking_cost import calculate_booking_cost

def test_1_night():
    assert calculate_booking_cost(1, 10000) == 10000

def test_multiple_nights():
    assert calculate_booking_cost(3, 5000) == 15000

def test_zero_rate():
    assert calculate_booking_cost(5, 0) == 0

def test_boundary_max_nights():
    assert calculate_booking_cost(30, 100) == 3000

def test_boundary_min_nights():
    assert calculate_booking_cost(1, 1) == 1

def test_nights_zero_invalid():
    with pytest.raises(ValueError):
        calculate_booking_cost(0, 1000)

def test_nights_31_invalid():
    with pytest.raises(ValueError):
        calculate_booking_cost(31, 1000)

def test_nights_negative_invalid():
    with pytest.raises(ValueError):
        calculate_booking_cost(-1, 1000)

def test_rate_negative_invalid():
    with pytest.raises(ValueError):
        calculate_booking_cost(2, -1)

def test_nights_string_type_error():
    with pytest.raises(TypeError):
        calculate_booking_cost("2", 1000)

def test_nights_float_type_error():
    with pytest.raises(TypeError):
        calculate_booking_cost(2.5, 1000)

def test_nights_bool_type_error():
    with pytest.raises(TypeError):
        calculate_booking_cost(True, 1000)

def test_rate_bool_type_error():
    with pytest.raises(TypeError):
        calculate_booking_cost(2, False)