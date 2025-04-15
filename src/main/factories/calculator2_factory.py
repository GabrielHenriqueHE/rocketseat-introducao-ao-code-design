from src.domain.calculator.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    driver = NumpyHandler()

    return Calculator2(driver)