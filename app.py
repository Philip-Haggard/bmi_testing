# Importing Flask
from flask import Flask, request, render_template

app = Flask(__name__)

# This function calculates the bmi value given the weight and height of the person in pounds
def calculate_bmi_value(weight, height):
    bmi = round((weight * 0.45) / ((height * 0.025)*(height * 0.025)), 1)
    return bmi

# This function calculates the bmi category given the bmi value
def calculate_bmi_category(bmi):
    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        category = 'Normal weight'
    elif 25 <= bmi <= 29.9:
        category = 'Overweight'
    else:
        category = 'Obese'
    return category

# Flask implementation
@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        if weight > 0 and height > 0:
            bmi = calculate_bmi_value(weight, height)
            category = calculate_bmi_category(bmi)
    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
