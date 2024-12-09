import pytest
from src.calculadora.py import suma, resta, multiplicacion, division

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(3, 5) == -2
    assert resta(0, 0) == 0

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-2, 3) == -6
    assert multiplicacion(0, 5) == 0

def test_division():
    assert division(6, 2) == 3
    assert division(5, 1) == 5
    with pytest.raises(ValueError):
        division(1, 0)