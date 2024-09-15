from flask import Flask

app = Flask(__name__)

# Base URL - index view
@app.route('/')
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string in console and display it in the browser
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Prints the string to the console
    return parameter  # Displays the string in the browser

# Count numbers up to the given parameter
@app.route('/count/<int:number>')
def test_count_range_10(number):
    result = '\n'.join(str(i) for i in range(number + 1))  # Joins the range of numbers into separate lines
    return result

# Perform basic math operations
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # Division, using 'div' to avoid confusion with '/'
        result = num1 / num2
    elif operation == '%':  # Modulus operation
        result = num1 % num2
    else:
        return 'Invalid operation', 400  # Return error if the operation is invalid

    return str(result)  # Return the result as a string

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
