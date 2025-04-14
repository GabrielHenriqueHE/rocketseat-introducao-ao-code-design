from pytest import raises

from typing import Dict

from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock = MockRequest({
        'number': 1
    })

    calculator1 = Calculator1()

    response = calculator1.calculate(mock)

    assert 'data' in response
    assert 'calculator' in response['data']
    assert 'result' in response['data']

    assert response['data']['result'] == 14.25
    assert response['data']['calculator'] == 1

def test_calculate_with_malformed_body_error():
    mock = MockRequest({
        'data': 1
    })

    calculator1 = Calculator1()

    with raises(Exception) as exception_info:
        calculator1.calculate(mock)

    assert str(exception_info.value == "Body mal formatado!")
