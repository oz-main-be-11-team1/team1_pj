from config import db


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # nullable=False 제거
    choice_id = db.Column(db.Integer, db.ForeignKey('choices.id')) # nullable=False 제거
    user = db.relationship('Users', back_populates='answers')
    choice = db.relationship('Choices', back_populates='answers')

class Choices(db.Model):
    __tablename__ = 'choices'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    sqe = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    question = db.relationship('Question', back_populates='choices')
    answers = db.relationship('Answer', back_populates='choice')

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Enum('teen', 'twenty', 'thirty', 'forty', 'fifty', name='age_enum'), nullable=False)
    gender = db.Column(db.Enum('male', 'female', name='gender_enum'), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    answers = db.relationship('Answer', back_populates='user')

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    sqe = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


    image = db.relationship('Images', back_populates='questions')
    choices = db.relationship('Choices', back_populates='question')

class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('main', 'sub', name='image_type_enum'), nullable=False) # name 지정 권장
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    questions = db.relationship('Question', back_populates='image')