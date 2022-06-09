from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return 'This is a home page'


@app.route('/about')
def about():
    return 'This is about us page'


@app.route('/staff')
def staff():
    employees = {'n1': 'l1', 'n2': 'l2', 'n3': 'l3'}
    return render_template('user.html', emp=employees)


if __name__ == "__main__":
    app.run(debug=True)