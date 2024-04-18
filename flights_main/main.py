from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'

CORS(app)

db = SQLAlchemy(app)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.String(db.String(200))
    departure_date = db.Column(db.Date)

class FlightUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    flight_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'flight_id', name='uniq_user_flight')


@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')