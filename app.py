from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from faker import Faker


app = Flask(__name__)
app.config['DEBUG'] = False
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'SECRET_KEY-FOR-LILAB'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:secure_pass_here@localhost:5432/lilab"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
fake = Faker()
ma = Marshmallow(app)


@app.route('/')
def hello():
    return render_template('index.html')

from clients.controllers_client import *
from credits.controllers import *

if __name__ == '__main__':
    app.run()