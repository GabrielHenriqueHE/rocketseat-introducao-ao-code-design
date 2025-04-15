from src.domain.calculator.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

def calculator3_factory():
    driver = NumpyHandler()

    return Calculator3(driver)