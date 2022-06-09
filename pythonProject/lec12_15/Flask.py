from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.config['SECRET-KEY'] = 'Python'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('user', name=username))
    return render_template('login.html')


@app.route('/<name>')
def user(name):
    subjects = ['python', 'calculus', 'DB']
    return render_template('user.html', my_name=name, subjects=subjects)


@app.route('/<name>/<age>')
def userage(name, age):
    return f'Hello {name}, your age is {age}'


@app.route('/admin')
def admin():
    # return redirect('https://www.google.com/')
    # return redirect('/')
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)


if __name__ == "__main__":
    app.run(debug=True)
