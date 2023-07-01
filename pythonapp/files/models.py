from . import db;
from sqlalchemy.sql import func;

class Record(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    note = db.Column(db.String(300))
    status = db.Column(db.String(20),default='UNCOMPLETED')
    date = db.Column(db.DateTime(timezone=True),default=func.now())