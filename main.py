##################################################
#
# This program allows a user to enter their
# height and weight and will return their
# BMI value and category
#
##################################################

class BMI:

    def bmi_category_calculation(self, x):
            if x < 18.5:
                return "Underweight"
            elif x >= 18.5 and x < 25:
                return "Normal weight"
            elif x >= 25 and x < 30:
                return "Overweight"
            else:
                return "Obese"
        
    def bmi_value_calculation(self):
        height = input("Please enter your height in feet and inches (example: 5 9 or 6 2): ")
        height_ft, height_in, *_ = map(int, height.split())
        weight = float(input("Please enter your weight in pounds: "))

        if height_ft < 0 or height_in < 0:
            raise ValueError("Height must be positive!")
        elif height_ft == 0:
             raise ValueError("Height must be greater than zero!")
        elif height_in > 11:
             raise ValueError("Height in inches must be less than 12!")
        elif weight < 0:
             raise ValueError("Weight must be greater than zero!")
        elif weight == 0:
             raise ValueError("Weight must be greater than zero!")

        bmi_value = (weight * 0.45) / ((((height_ft*12) + height_in) * 0.025) ** 2)
        category = self.bmi_category_calculation(bmi_value)
        output = "Your BMI is " + str(round(bmi_value)) + " and you are " + category + "."
        
        return output

def main():
     bmi = BMI()
     print(bmi.bmi_value_calculation())

if __name__ == "__main__":
     main()