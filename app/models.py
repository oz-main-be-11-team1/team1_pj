from config import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    choices = db.relationship('Choices', backref='question', lazy=True)


class Choices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    choice_text = db.Column(db.String(200), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    answers = db.relationship('Answer', backref='choice', lazy=True)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    choice_id = db.Column(db.Integer, db.ForeignKey('choices.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
