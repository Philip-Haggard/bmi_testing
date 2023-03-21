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

def test_negative_weight(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 9\n' if 'height' in prompt else '-1\n')
    bmi = BMI()
    with pytest.raises(ValueError) as exc_info:
        bmi.bmi_value_calculation()
    assert str(exc_info.value) == "Weight must be greater than zero!"

def test_zero_weight(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 9\n' if 'height' in prompt else '0\n')
    bmi = BMI()
    with pytest.raises(ValueError) as exc_info:
        bmi.bmi_value_calculation()
    assert str(exc_info.value) == "Weight must be greater than zero!"

def test_negative_height_feet(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '-5 9\n' if 'height' in prompt else '150\n')
    bmi = BMI()
    with pytest.raises(ValueError) as exc_info:
        bmi.bmi_value_calculation()
    assert str(exc_info.value) == "Height must be positive!"

def test_negative_height_inches(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 -9\n' if 'height' in prompt else '150\n')
    bmi = BMI()
    with pytest.raises(ValueError) as exc_info:
        bmi.bmi_value_calculation()
    assert str(exc_info.value) == "Height must be positive!"

def test_zero_height_feet(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '0 0\n' if 'height' in prompt else '150\n')
    bmi = BMI()
    with pytest.raises(ValueError) as exc_info:
        bmi.bmi_value_calculation()
    assert str(exc_info.value) == "Height must be greater than zero!"

def test_too_positive_height_inches(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '5 12\n' if 'height' in prompt else '150\n')
    bmi = BMI()
    with pytest.raises(ValueError) as exc_info:
        bmi.bmi_value_calculation()
    assert str(exc_info.value) == "Height in inches must be less than 12!"







