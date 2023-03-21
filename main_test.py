import pytest
from main import BMI

def gen_inputs():
    inputs = ["5 9", "160"]

    for item in inputs:
        yield item

GEN = gen_inputs()

def test_value_calculation(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    bmi = BMI()
    assert bmi.bmi_value_calculation() == "Your BMI is 24 and you are Normal weight."

def test_underweight_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(13) == "Underweight"

def test_normal_weight_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(22) == "Normal weight"

def test_overweight_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(27) == "Overweight"

def test_obese_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(35) == "Obese"