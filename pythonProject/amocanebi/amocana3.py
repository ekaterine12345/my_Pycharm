from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oscar.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Oscar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    movie = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return f"id {self.id}, year {self.year}, age {self.age}, name {self.name}, gender {self.gender}, movie {self.movie}"


db.create_all()

oscar = Oscar(id=1, year=1928, age=44, name='Emil Jannings', gender='M', movie='The Last Command - The Way of All Flash')
db.session.add(oscar)
db.session.commit()
