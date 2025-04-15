from typing import List, Dict
from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator3:
    '''
    * N números são colocados como entrada.

    * Caso a variância de todos esses números for menor que a multplicação deles é apresentado uma informação de sucesso ao usuário.

    * Caso contrário, é apresentado uma informação de falha.
    '''

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_result(variance, multiplication)

        return self.__format_response(variance)

    
    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError(message='Body mal formatado!')

        input_data = body['numbers']
        return input_data
    
    def __calculate_variance(self, input_data: List[float]) -> float:
        return self.__driver_handler.variance(input_data)
    
    def __calculate_multiplication(self, input_data: List[float]) -> float:
        result = 1
        for number in input_data: result *= number
        return result
    
    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError('Falha no processo. Variância menor que multiplicação.')
        
    def __format_response(self, variance: float) -> Dict:
        return {
            'data': {
                'calculator': 3,
                'result': float(variance),
                'success': True
            }
        }