import pytest

from ..modules.calcul import square

def test_square_with_positive_int():
    integer = 2
    assert square(integer) == integer ** 2

def test_square_with_negative_int():
    integer = -2
    assert square(integer) == integer ** 2

def test_square_with_float():
    with pytest.raises(TypeError):
        square(2.5)
