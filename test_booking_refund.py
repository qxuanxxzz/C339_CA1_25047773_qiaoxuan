import pytest
from booking_refund import is_refundable

def test_refund_flexible_48_hours():
    assert is_refundable(48, True) is True

def test_refund_flexible_more_than_48():
    assert is_refundable(100, True) is True

def test_no_refund_flexible_47_hours():
    assert is_refundable(47, True) is False

def test_no_refund_non_flexible_48():
    assert is_refundable(48, False) is False

def test_no_refund_non_flexible_100():
    assert is_refundable(100, False) is False

def test_no_refund_flexible_zero_hours():
    assert is_refundable(0, True) is False

def test_hours_negative_value_error():
    with pytest.raises(ValueError):
        is_refundable(-1, True)

def test_hours_string_type_error():
    with pytest.raises(TypeError):
        is_refundable("48", True)

def test_hours_bool_type_error():
    with pytest.raises(TypeError):
        is_refundable(True, True)

def test_flexible_not_bool_type_error():
    with pytest.raises(TypeError):
        is_refundable(48, "True")

def test_flexible_int_not_bool_type_error():
    with pytest.raises(TypeError):
        is_refundable(48, 1)
