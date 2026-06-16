import pytest
from app.operation.operations import Add, Subtract, Multiply, Divide


@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0)
    ]
)
def test_add(a, b, result):
    assert Add.calculate(a, b) == result


@pytest.mark.parametrize(
    "a,b,result",
    [
        (5, 3, 2),
        (10, 5, 5),
        (-1, 1, -2)
    ]
)
def test_subtract(a, b, result):
    assert Subtract.calculate(a, b) == result


@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 3, 6),
        (10, 5, 50),
        (-1, 5, -5)
    ]
)
def test_multiply(a, b, result):
    assert Multiply.calculate(a, b) == result


@pytest.mark.parametrize(
    "a,b,result",
    [
        (10, 2, 5),
        (20, 4, 5),
        (-10, 2, -5)
    ]
)
def test_divide(a, b, result):
    assert Divide.calculate(a, b) == result


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide.calculate(10, 0) 