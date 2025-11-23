from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    note = db.Column(db.String(255))

    def __repr__(self):
        return f"<Expense {self.id} {self.category} {self.amount}>"
