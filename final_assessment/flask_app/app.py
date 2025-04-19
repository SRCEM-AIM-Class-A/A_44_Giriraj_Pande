from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Displays a "Hello, World!" message on the homepage.
    # 2. Has a second route that displays a form to accept a user's name and
    #    age, and returns a greeting message with these inputs.
    return render_template('home.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    error = None
    if request.method == 'POST':
        name = request.form['name'].strip()
        age = request.form['age'].strip()

        # Implements basic error handling for invalid inputs.
        # Validate name: only letters and spaces
        if not name or not re.match("^[A-Za-z ]+$", name):
            error = "Please enter a valid name (letters and spaces only)."
        elif not age.isdigit() or int(age) <= 0:
            error = "Please enter a valid positive age."
        else:
            return render_template('greet.html', name=name, age=age)

    return render_template('form.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)