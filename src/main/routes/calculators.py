from flask import Blueprint, jsonify, request

from src.drivers.numpy_handler import NumpyHandler

from src.domain.calculator.calculator_1 import Calculator1
from src.domain.calculator.calculator_2 import Calculator2

calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():

    calc = Calculator1()
    response = calc.calculate(request)

    return jsonify(response), 200

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_2():

    driver = NumpyHandler()

    calc = Calculator2(driver)
    response = calc.calculate(request)

    return jsonify(response), 200