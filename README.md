# 🎬 설문조사 서비스 (Back-End)

소개 적을란

## 👨‍💻 팀원 소개

| 이름  |      역할      | 
|:---:|:------------:| 
| 정성운 | 팀장, Back-End |
| 박동재 | 팀원, Back-End | 
| 임우진 | 팀원, Back-End |
| 양지웅 | 팀원, Back-End |

## 📅 프로젝트 기간

* 2025.06.11 ~ 2025.06.13

## ✨ 주요 기능

### 👤 Accounts
- **회원가입**

### 🎞️ Questions
- **질문 작성** 및 전체 조회
- 질문 **갯수** 조회

### 📝 Answers, Choices, Images, status_routes
- **답변 저장** 및 선택지 생성
- 이미지 업로드 및 조회
- 사용 중인 유저의 각 질문당 선택지 선택 비율 조회
- 모든 질문에 대해 각 선택지의 선택 횟수 및 비율 조회
- 답변에 대한 통계 정보 제공


## 🛠️ 기술 스택

| 구분 |   내용   |
| :--: |:------:|
| **언어** | Python |
| **프레임워크** | Flask  |
| **데이터베이스** | Mysql  |
| **API** | Flask  |
| **배포** | AWS EC2  |
| **버전 관리** | Git  |

## 🚀 프로젝트 실행 방법

```bash
# 1. 원격 저장소 복제
$git clone [https://github.com/oz-main-be-11-team1/team1_pj.git$](https://github.com/oz-main-be-11-team1/team1_pj.git$) cd team1_pj

# 2. 가상환경 생성 및 실행
$python -m venv venv$ source venv/Scripts/activate

# 3. 필요한 패키지 설치
$ pip install -r requirements.txt

# 4. 데이터베이스 초기 설정
$ flask db upgrade
```

## 📖 API Endpoint

> `http://127.0.0.1:8000/`

| Method        | URL                                  | 설명                            |
|:--------------|:-------------------------------------|:------------------------------|
| **Accounts**  |                                      |                               |
| `POST`        | `/signup`                            | 회원가입                          |
| **questions** |                                      |                               |
| `GET`         | `/questions/count`                   | 전체 질문 갯수 가져오기                 |
| `GET`         | `/questions/<int:question_id>`       | 특정 질문 가져오기                    |
| `POST`        | ` /question`                         | 새 질문 작성                       
| **Answer**    |                                      |                               |
| `GET`         | `/submit`                            | 답변 저장                         |
| choice        |||
| `POST`        | `/choice`                            | 선택지 생성                        |
| images        |                                      |                               |
| `POST`        | `/images`                            | 이미지 업로드                       |
| `GET`         | `/main`                              | 메인 이미지 조회                     |
| status_routes |||
|  `GET`        | `/stats/answer_rate_by_choice`       | 사용 중인 유저의 각 질문당 선택지 선택 비율 |
| `GET`         | `/stats/answer_count_by_question`    | 모든 질문에 대해 각 선택지의 선택 횟수 및 비율      |

## 📂 디렉토리 구조

```
team1_pj
├── .git
├── accounts/           # 유저/인증 관련 앱
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── team1_pj/           # 프로젝트 설정
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
