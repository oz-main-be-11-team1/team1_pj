from flask import request, Blueprint, jsonify

from app.models import Answer
from config import db

answers_blp = Blueprint("answers", __name__)


@answers_blp.route("/submit", methods=["POST"])
def submit_answer():
    data = request.get_json()
    if not all(k in data for k in ["user_id", "choice_id"]):
        return jsonify({"error": "존재하지 않는 필드입니다"}), 400

    answer = Answer(
        user_id=data["user_id"],
        choice_id=data["choice_id"]
    )

    db.session.add(answer)
    db.session.commit()

    return jsonify({"message": "답변이 정상적으로 등록 되었습니다"}), 201