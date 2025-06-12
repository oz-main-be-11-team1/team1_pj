from flask import jsonify, Blueprint, request
from ..models import Choices, db, Question  # 상대 경로 유지

choices_blp = Blueprint('choices_blp',__name__)

@choices_blp.route('/choice', methods=['POST'])
def create_choice():
    data = request.get_json()
    if not all(k in data for k in ['content', 'is_active', 'sqe', 'question_id']):
        return jsonify({'error': 'Missing fields'}), 400
    if not Question.query.get(data['question_id']):
        return jsonify({'error': 'Invalid question_id'}), 400
    choice = Choices(
        content=data['content'],
        is_active=data['is_active'],
        sqe=data['sqe'],
        question_id=data['question_id']
    )
    db.session.add(choice)
    db.session.commit()
    return jsonify({
        'message': '새로운 선택지가 성공적으로 생성되었습니다',
    }), 201
