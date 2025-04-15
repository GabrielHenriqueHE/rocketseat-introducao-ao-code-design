from typing import Dict, List
from pytest import raises

from src.drivers.numpy_handler import NumpyHandler
from src.domain.calculator.calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

class MockDriverHandler:
    def variance(self, numbers: List[int]) -> float:
        return 100
    
class MockDriverHandlerError:
    def variance(self, numbers: List[int]) -> float:
        return 3

def test_calculate():
    mock = MockRequest({
        'numbers': [1, 1, 1, 1, 100]
    })

    calculator3 = Calculator3(MockDriverHandler())

    response = calculator3.calculate(mock)

    print(response)

def test_calculate_with_minor_variance_error():
    calculator3 = Calculator3(MockDriverHandlerError())

    mock = MockRequest({
            'numbers': [1, 2, 3, 4, 5]
        })

    with raises(Exception) as exception_info:
        calculator3 = Calculator3(NumpyHandler())

        calculator3.calculate(mock)
    
    assert str(exception_info.value) == 'Falha no processo. Variância menor que multiplicação.'
