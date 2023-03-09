##################################################
#
# This program allows a user to enter their
# height and weight and will return their
# BMI value and category
#
##################################################

def bmi_value_calculation(x, y):
    bmi_value = (y * 0.45) / ((x * 0.025) ** 2)
    return round(bmi_value, 2)

def bmi_category_calculation(x):
    if x < 18.5:
        category = "Underweight"
    elif x >= 18.5 and x < 25:
        category = "Normal weight"
    elif x >= 25 and x < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return category


# prompting the user for their height
print("Please enter your height in inches: ")
height = int(input())

# prompting the user for their weight
print("Please enter your weight in pounds: ")
weight = int(input())

# calculating BMI value
bmi_value = bmi_value_calculation(height, weight)

# calculating BMI category
bmi_category = bmi_category_calculation(bmi_value)

print("Your BMI value is " + str(bmi_value))
print ("Your BMI category is " + str(bmi_category))
