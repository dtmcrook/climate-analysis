from temp_conversion import fahr_to_kelvin
from nose.tools import *
def fahr_to_kelvin_basic():
    assert fahr_to_kelvin(20.0)==244

def fahr_to_kelvin_zero():
    assert round(fahr_to_kelvin(-459.67),2)==0.00

@raises(TypeError)
def test_temp_string():
    assert fahr_to_kelvin("SomeTemperature")

@raises(TypeError)
def test_temp_string():
    assert fahr_to_kelvin()


