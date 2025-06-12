from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from app.models import Users
from config import db

user_blp = Blueprint('users', __name__)
@user_blp.route('/', methods=['GET'])
def connect():
        return jsonify({'message': 'Connected'})

@user_blp.route('/signup', methods=['POST'])
def signup_page():
    try:
        data = request.get_json()
        user = Users(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            email=data["email"],
        )
        db.session.add(user)
        db.session.commit()
        return (
            jsonify(
                {
                    "message": f"{user.name}님 회원가입을 축하합니다",
                    "user_id": user.id,
                }
            ),
            201,
        )
    except KeyError as e:
        return jsonify({"message": f"Missing required field: {str(e)}"}), 400

    except ValueError:
        return jsonify({"message": "이미 존재하는 계정 입니다."}), 400

    except IntegrityError:
        return jsonify({"message": "이미 존재하는 이메일 입니다."}), 400