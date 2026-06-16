import pytest
from app.calculation.calculation import CalculationFactory


@pytest.mark.parametrize(
    "operation,a,b,result",
    [
        ("add", 5, 5, 10),
        ("subtract", 10, 5, 5),
        ("multiply", 5, 5, 25),
        ("divide", 20, 4, 5)
    ]
)
def test_factory_operations(operation, a, b, result):
    calculation = CalculationFactory.create_calculation(
        operation,
        a,
        b
    )

    assert calculation.perform() == result


def test_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create_calculation(
            "invalid",
            1,
            1
        ) 