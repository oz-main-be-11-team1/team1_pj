from flask import request, Blueprint, jsonify
from app.models import Question, Images, Choices
from config import db

questions_blp = Blueprint('questions_blp', __name__)

@questions_blp.route('/question', methods=['POST'])
def create_questions():
    try:
        data = request.get_json()
        image = Images.query.get(data['image_id'])
        if not image:
            return jsonify({'error': 'Invalid image_id'}), 400
        question = Question(
            title=data['title'],
            sqe=data['sqe'],
            image_id=data['image_id'],
            is_active=data['is_active'],
        )

        db.session.add(question)
        db.session.commit()

        return jsonify(
            {"message": f"Title: {question.title} 질문이 성공적으로 생성 되었습니다"}
        ), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400

@questions_blp.route('/questions/<int:question_sqe>', methods=['GET'])
def get_question(question_sqe):

    question = Question.query.filter_by(sqe=question_sqe, is_active=True).first()

    if not question:
        return jsonify({"error": "해당 질문이 존재하지 않습니다"}), 404

    image = Images.query.get(question.image_id)

    choice_list = (
        Choices.query.filter_by(question_id=question_sqe, is_active=True)
        .order_by(Choices.sqe)
        .all()
    )

    return jsonify(
        {
            "id": question.id,
            "title": question.title,
            "image": image.url if image else None,
            "choices": [choice.to_dict() for choice in choice_list]
        }
    )

@questions_blp.route("/questions/count", methods=["GET"])
def count_question():
        count = len(Question.query.filter_by(is_active=True).all())
        return jsonify({"total": count})


