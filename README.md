# ⚗️🧪 Flask Seminar for Agile Course

## The instructions to make your own Flaks App

### Virtual environment

The very first step to Flask is the usual one.
Make a repo, clone, navigate into, open in VSCode.

Then it is a good idea to have a virtual environment for your Python. Make sure to check the Python version first.

```bash
python3 -m venv myenv
```

Activate the environment.

```bash
source myenv/bin/activate
```

## The first Flask app

Once your virtual envronment is activated install Flask.

```bash
pip install flask
```

Then create  a file called `app.py`.

Add the code below to start:

```python
from flask import Flask  # Importing the Flask module

app = Flask(__name__)  # Creating a Flask application instance with the name of the current module (__name__)

@app.route('/')  # Define a route for the root URL

def home():  # Define a view function for the root URL
    return 'Hello, Flask!'  # Return a simple response

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode if this script is executed directly
```

Now in the terminal run the following command:

```bash
python3 app.py
```

At the url `http://127.0.0.1:5000` you will see the output of function `home()`.

Yes, funciton `home()` just gest invoked without being called. Flask magic.

## Using html templating to make UI

To start adding nice HTML to out Python app, first change the `app.py`.

```python
from flask import Flask, render_template  # Import the Flask module and render_template function

app = Flask(__name__)  # Create a Flask application instance with the name of the current module (__name__)

@app.route('/')  # Define a route for the root URL
def home():  # Define a view function for the root URL
    return render_template('index.html')  # Render the 'index.html' template

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode if this script is executed directly
```

Then create a folder in the root called `templates`.
Inside folder `templates` make an `index.html` file.

Suggested first index.html content is below:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome, students</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Welcome, students</h1>
</body>
</html>
```

Now make a folder called `static` and add `styles.css`.

Suggest content:

```css
h1 {
    color: #ff0000;
    text-align: center;
    font-family: Arial, sans-serif;
}
```