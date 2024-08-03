from app.models import db


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('questions', lazy=True))
    responses = db.relationship('Response', backref='question', lazy=True)

    def __repr__(self):
        return f'Question: {self.text}'
