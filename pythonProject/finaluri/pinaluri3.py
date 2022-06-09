from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///article.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    view = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    dislikes = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f'''user_id {self.user_id}, name {self.name}, category {self.category},
                    view {self.view}, likes {self.likes}, dislikes {self.dislikes}, comments {self.comments} '''

db.create_all()

article = Article(user_id=2, name='python insert', category='python', view=15, likes=17, dislikes=0, comments=0)
print(article)
db.session.add(article)
db.session.commit()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()