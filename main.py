import pytest
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todos.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


app.app_context().push()

# @pytest.fixture(autouse=True)
# def app_context():
#     app = Flask(__name__)
#     with app.app_context():
#         yield
        
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"



@app.route('/')
def hello_world():
    todo=Todo(title="hey",desc="hhh")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')
@app.route('/home')
def sum():
    return "5"
@app.route('/show')
def show():
    allTodo=Todo.query.all()
    print(allTodo)
    return "this is product"

if __name__ == '__main__':
    app.run(debug=True,port=8000)