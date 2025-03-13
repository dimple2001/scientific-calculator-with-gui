from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Store calculation history
calculation_history = []

@app.route('/')
def index():
    # Flask automatically looks for HTML files inside the 'templates' folder
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    result = None
    error = None
    
    try:
        if operation == 'calculate':
            expression = data.get('expression')
            expression = expression.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            calculation_history.append(f"{expression} = {result}")
            
        elif operation == 'sqrt':
            value = float(data.get('value'))
            if value < 0:
                error = "Cannot calculate square root of a negative number"
            else:
                result = math.sqrt(value)
                calculation_history.append(f"sqrt({value}) = {result}")
                
        elif operation == 'factorial':
            value = int(float(data.get('value')))
            if value < 0:
                error = "Factorial is only defined for positive integers"
            else:
                result = math.factorial(value)
                calculation_history.append(f"{value}! = {result}")
                
        elif operation == 'sin':
            value = float(data.get('value'))
            result = math.sin(math.radians(value))
            calculation_history.append(f"sin({value}) = {result}")
            
        elif operation == 'cos':
            value = float(data.get('value'))
            result = math.cos(math.radians(value))
            calculation_history.append(f"cos({value}) = {result}")
            
        elif operation == 'tan':
            value = float(data.get('value'))
            result = math.tan(math.radians(value))
            calculation_history.append(f"tan({value}) = {result}")
            
        elif operation == 'log':
            value = float(data.get('value'))
            if value <= 0:
                error = "Cannot calculate logarithm of zero or negative number"
            else:
                result = math.log10(value)
                calculation_history.append(f"log({value}) = {result}")
                
        elif operation == 'ln':
            value = float(data.get('value'))
            if value <= 0:
                error = "Cannot calculate natural logarithm of zero or negative number"
            else:
                result = math.log(value)
                calculation_history.append(f"ln({value}) = {result}")
        
        if error:
            return jsonify({'success': False, 'error': error})
        else:
            return jsonify({'success': True, 'result': result})
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    global calculation_history
    calculation_history = []
    return jsonify({'success': True})

@app.route('/get_history', methods=['GET'])
def get_history():
    return jsonify({'history': calculation_history})

if __name__ == '__main__':
    app.run(debug=True)
