import pytest
from main import BMI

##############################
# CATEGORY CALCULATION TESTS #
##############################

def test_underweight_upper_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(18.4) == "Underweight"

def test_normal_weight_lower_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(18.5) == "Normal weight"

def test_normal_weight_middle_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(22) == "Normal weight"

def test_normal_weight_upper_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(24.9) == "Normal weight"

def test_overweight_lower_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(25) == "Overweight"

def test_overweight_middle_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(27) == "Overweight"

def test_overweight_upper_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(29.9) == "Overweight"

def test_obese_lower_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(30) == "Obese"

def test_obese_middle_category():
    bmi = BMI()
    assert bmi.bmi_category_calculation(35) == "Obese"

###############################
# BMI VALUE CALCULATION TESTS #
###############################

def underweight_inputs():
    inputs = ["6 0", "125"]

    for item in inputs:
        yield item

UNDERWEIGHT = underweight_inputs()

def normal_weight_inputs():
    inputs = ["5 3", "125"]

    for item in inputs:
        yield item

NORMALWEIGHT = normal_weight_inputs()

def overweight_inputs():
    inputs = ["5 9", "185"]

    for item in inputs:
        yield item

OVERWEIGHT = overweight_inputs()

def obese_inputs():
    inputs = ["5 5", "220"]

    for item in inputs:
        yield item

OBESE = obese_inputs()

def test_underweight_bmi(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(UNDERWEIGHT))
    bmi = BMI()
    assert bmi.bmi_value_calculation() == "Your BMI is 17.4 and you are Underweight."

def test_normal_weight_bmi(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(NORMALWEIGHT))
    bmi = BMI()
    assert bmi.bmi_value_calculation() == "Your BMI is 22.7 and you are Normal weight."

def test_overweight_bmi(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(OVERWEIGHT))
    bmi = BMI()
    assert bmi.bmi_value_calculation() == "Your BMI is 28.0 and you are Overweight."

def test_obese_bmi(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(OBESE))
    bmi = BMI()
    assert bmi.bmi_value_calculation() == "Your BMI is 37.5 and you are Obese."

####################################################################################

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