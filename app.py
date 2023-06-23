from flask import Flask, render_template, request  # Import the Flask module and render_template function

app = Flask(__name__)  # Create a Flask application instance with the name of the current module (__name__)

@app.route('/')  # Define a route for the root URL
def home():  # Define a view function for the root URL
    return render_template('index.html')  # Render the 'index.html' template

@app.route('/greet', methods=['POST']) # Define a route for the /greet
def greet():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode if this script is executed directly
