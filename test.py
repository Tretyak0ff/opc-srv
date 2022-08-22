import pytest
from model import Analog, Digital


def test_get_model_analog():
    valve_analog_1 = Analog()
    valve_analog_1 = str(type(valve_analog_1))
    assert valve_analog_1 == "<class 'model.Analog'>"


def test_get_model_digital():
    valve_digital_1 = Digital()
    valve_digital_1 = str(type(valve_digital_1))
    assert valve_digital_1 == "<class 'model.Digital'>"


def test_get_model_analog_negative():
    valve_analog_1 = Analog()
    valve_analog_1 = str(type(valve_analog_1))
    assert valve_analog_1 == "<class 'model.Digital'>"


def test_get_model_digital_negative():
    valve_digital_1 = Digital()
    valve_digital_1 = str(type(valve_digital_1))
    assert valve_digital_1 == "<class 'model.Analog'>"