from flask import Blueprint, request, jsonify  # Flask에서 Blueprint(라우터 분리), request(입력), jsonify(응답 변환) 사용
from app.models import db, Images  # DB 인스턴스와 Image 모델을 import

# Blueprint 인스턴스 생성: '/image'로 시작하는 API 라우터 정의
images_blp = Blueprint('image', __name__, url_prefix='/image')


# GET /image/main - 최신 메인 이미지 하나 조회
@images_blp.route('/main', methods=['GET'])
def get_main_image():
    # type이 'main'인 이미지 중 가장 최신(created_at 내림차순) 하나를 가져옴
    main_image = Images.query.filter_by(type='main').order_by(Images.created_at.desc()).first()

    # 없다면 404 반환
    if not main_image:
        return jsonify({"image": None}), 404

    # 있다면 해당 이미지의 URL 반환
    return jsonify({"image": main_image.url})


# POST /image - 이미지 등록
@images_blp.route('', methods=['POST'])
def create_image():
    data = request.get_json()  # 요청에서 JSON 데이터 가져오기
    url = data.get('url')  # 'url' 필드 추출
    img_type = data.get('type')  # 'type' 필드 추출

    # 유효성 검사: url이 없거나 type이 'main' 또는 'sub' 가 아니면 오류 반환
    if not url or img_type not in ['main', 'sub']:
        return jsonify({"message": "Invalid data"}), 401

    # Image 모델 인스턴스 생성
    new_image = Images(url=url, type=img_type)

    # DB에 추가 및 커밋
    db.session.add(new_image)
    db.session.commit()

    # 성공 메시지 반환
    return jsonify({"message": f"{new_image.id}가 등록되었습니다 "}), 201