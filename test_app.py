import pytest
from app import calculate_bmi_value
from app import calculate_bmi_category

# Category Calculation Tests

def test_underweight_upper_category():
    assert calculate_bmi_category(18.4) == ('Underweight')

def test_normal_weight_lower_category():
    assert calculate_bmi_category(18.5) == ('Normal weight')

def test_normal_weight_middle_category():
    assert calculate_bmi_category(22) == ('Normal weight')

def test_normal_weight_upper_category():
    assert calculate_bmi_category(24.9) == ('Normal weight')

def test_overweight_lower_category():
    assert calculate_bmi_category(25) == ('Overweight')

def test_overweight_middle_category():
    assert calculate_bmi_category(27) == ('Overweight')

def test_overweight_upper_category():
    assert calculate_bmi_category(29.9) == ('Overweight')

def test_obese_lower_category():
    assert calculate_bmi_category(30) == ('Obese')

def test_obese_middle_category():
    assert calculate_bmi_category(35) == ('Obese')

# BMI Value Calculation Tests

def test_underweight_bmi_value_calculation():
    assert calculate_bmi_value(125, 72) == (17.4)

def test_normal_weight_bmi_value_calculation():
    assert calculate_bmi_value(125, 63) == (22.7)

def test_overweight_bmi_value_calculation():
    assert calculate_bmi_value(185, 69) == (28.0)

def test_obese_bmi_value_calculation():
    assert calculate_bmi_value(220, 65) == (37.5)
