from typing import Dict, List

from src.domain.calculator.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def standard_deviation(self, numbers: List[float]) -> float:
        return 0.2

def test_calculate():

    mock = MockRequest({
        'numbers': [1.5, 2.0, 2.5, 3.0]
    })

    driver = MockDriverHandler()

    calculator2 = Calculator2(driver)
    formatted_response = calculator2.calculate(mock)
    
    assert isinstance(formatted_response, Dict)
    assert formatted_response == {
        'data': {
            'calculator': 2,
            'result': 5.0
        }
    }

def test_calculate_with_numpy_handler():
    mock = MockRequest({
        'numbers': [1.5, 2.0, 2.5, 3.0]
    })

    driver = NumpyHandler()

    calculator2 = Calculator2(driver)
    formatted_response = calculator2.calculate(mock)
    
    assert isinstance(formatted_response, Dict)
    assert formatted_response == {
        'data': {
            'calculator': 2,
            'result': 0.2
        }
    }