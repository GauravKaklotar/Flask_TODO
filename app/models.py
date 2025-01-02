from . import db
from datetime import date

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date, nullable=True)  

    def __repr__(self):
        return f"<Todo {self.id} - {self.title}>"
