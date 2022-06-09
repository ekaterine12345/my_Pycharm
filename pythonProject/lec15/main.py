from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f'Book title:{self.title}; Author: {self.author}; Price: {self.price}'


# b1 = Books.query.first()
# print(b1)
# all_books = Books.query.filter_by(author='აკაკი წერეთელი').all()
#
# for each in all_books:
#     print(each)

# b1 = Books(title='ლექსების კრებული', author='აკაკი წერეთელი', price=15)
# db.session.add(b1)
# db.session.commit()

@app.route('/')
def home():
    all_books = Books.query.all()
    return render_template('index.html', all_books=all_books)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('user'))

    return render_template('login.html')


@app.route('/user')
def user():
    subjects = ['Python', 'Calculus', 'DB']
    return render_template('user.html',  subjects=subjects)


@app.route('/<name>/<age>')
def userage(name, age):
    return f'Hello {name}, your age is {age}'


@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        t = request.form['title']
        a = request.form['author']
        p = request.form['price']
        if t == '' or a == '' or p == '':
            flash('please enter all fields', 'error')
        elif not p.isnumeric():
            flash('price should be number', 'error')
        else:
            b1 = Books(title=t, author=a, price=float(p))
            print(b1)
            db.session.add(b1)
            db.session.commit()
            flash('dates added', 'info')
    return render_template('books.html')


if __name__ == "__main__":
    app.run(debug=True)
