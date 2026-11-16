import pytest
from main import calcular_area

def test_area_valores_enteros():
    assert calcular_area(5, 10) == 50

def test_area_valores_decimales():
    assert calcular_area(2.5, 4) == 10.0

def test_error_base_negativa():
    with pytest.raises(ValueError):
        calcular_area(-5, 10)

def test_error_altura_cero():
    with pytest.raises(ValueError):
        calcular_area(5, 0)