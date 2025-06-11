from flask import jsonify, Blueprint
from sqlalchemy import func
from config import db
from app.models import Answer, Choices, Question

stats_routes_blp = Blueprint('stats_routes', __name__)

# 1. 사용 중인 유저의 각 질문당 선택지 선택 비율
@stats_routes_blp.route('/stats/answer_rate_by_choice', methods=['GET'])
def user_answer_rate():
    try:
        result = db.session.query(
            Question.id.label('question_id'),
            Choices.id.label('choice_id'),
            func.count(Answer.id).label('answer_count'),
            (func.count(Answer.id) * 100 / func.sum(func.count(Answer.id)).over()).label('percentage')
        ).join(Choices, Choices.id == Answer.choice_id) \
         .join(Question, Question.id == Choices.question_id) \
         .group_by(Question.id, Choices.id) \
         .order_by(Question.id, Choices.id) \
         .all()

        data = [
            {
                "question_id": row.question_id,
                "choice_id": row.choice_id,
                "answer_count": row.answer_count,
                "percentage": round(row.percentage, 2)  # 소수점 2자리 반올림
            }
            for row in result
        ]

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 2. 모든 질문에 대해 각 선택지의 선택 횟수 및 비율
@stats_routes_blp.route('/stats/answer_count_by_question', methods=['GET'])
def question_answer_distribution():
    try:
        result = db.session.query(
            Question.id.label('question_id'),
            Choices.id.label('choice_id'),
            func.count(Answer.id).label('answer_count'),
            (func.count(Answer.id) * 100 / func.sum(func.count(Answer.id)).over(partition_by=Question.id)).label('percentage')
        ).join(Choices, Choices.id == Answer.choice_id) \
         .join(Question, Question.id == Choices.question_id) \
         .group_by(Question.id, Choices.id) \
         .order_by(Question.id, Choices.id) \
         .all()

        data = [
            {
                "question_id": row.question_id,
                "choice_id": row.choice_id,
                "answer_count": row.answer_count,
                "percentage": round(row.percentage, 2)  # 소수점 2자리 반올림
            }
            for row in result
        ]

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500