import main

def test_value_calculation():
    output = main.bmi_value_calculation(63,125)
    assert output == 22.68