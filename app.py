from flask import Flask, render_template, request
from typing import Union
app = Flask(__name__)

# --- Converstion Factors ---
# 1 inch = 2.54 cm

LENGTH_FACTORS = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1.0,
    'kilometer': 1000.0,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34
    
}

WEIGHT_FACTORS = {
    'milligram': 0.000001,
    'gram': 0.001,
    'kilogram': 1.0,
    'tonne': 1000.0,
    'ounce': 0.0283495,
    'pound': 0.453592,
    'stone': 6.35029
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    meters = value * LENGTH_FACTORS[from_unit]
    return meters / LENGTH_FACTORS[to_unit]

def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    kilograms = value * WEIGHT_FACTORS[from_unit]
    return kilograms / WEIGHT_FACTORS[to_unit]

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    # Convert to Celsius first
    c = value if from_unit == 'Celsius' else (value - 32) * 5/9 if from_unit == 'Fahrenheit' else value - 273.15
    # Convert from Celsius to target
    return c if to_unit == 'Celsius' else (c * 9/5) + 32 if to_unit == 'Fahrenheit' else c + 273.15

# -- Routes --
@app.route('/', methods=['GET', 'POST'])
@app.route('/length', methods=['GET', 'POST'])
def length_converter():
    result = Union[float, None] = None
    value = None
    from_unit = None
    to_unit = None

    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = round(convert_length(value, from_unit, to_unit), 4)
    return render_template('length.html', result=result, value=value, from_unit=from_unit, to_unit=to_unit, units=LENGTH_FACTORS.keys())

@app.route('/weight', methods=['GET', 'POST'])
def weight_converter():
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = round(convert_weight(value, from_unit, to_unit), 4)
        return render_template('weight.html', result=result, value=value, from_unit=from_unit, to_unit=to_unit, units=WEIGHT_FACTORS.keys())
    return render_template('weight.html', result=None, value=None, from_unit=None, to_unit=None, units=WEIGHT_FACTORS.keys())

@app.route('/temperature', methods=['GET', 'POST'])
def temperature_converter():
    TEMPERATURE_UNITS = ['Celsius', 'Fahrenheit', 'Kelvin']
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = round(convert_temperature(value, from_unit, to_unit), 4)
        return render_template('temp.html', result=result, value=value, from_unit=from_unit, to_unit=to_unit, units=TEMPERATURE_UNITS)
    return render_template('temp.html', result=None, value=None, from_unit=None, to_unit=None, units=TEMPERATURE_UNITS  )

if __name__ == '__main__':
    app.run(debug=True)
    
