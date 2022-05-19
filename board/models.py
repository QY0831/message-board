from datetime import datetime

# from Flask app import db object
# db object:
# <SQLAlchemy engine=sqlite:///Path/to/your/data.db>
from board import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
