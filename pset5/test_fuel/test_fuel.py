import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("0/1") == 0
    assert convert("1/2") == 50
    assert convert("4/4") == 100


def test_value_error():
    with pytest.raises(ValueError):
        convert("x/y")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"