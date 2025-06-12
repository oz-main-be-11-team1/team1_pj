from .answers import answers_blp
from .choices import choices_blp
from .questions import questions_blp
from .stats_routes import stats_routes_blp
from .users import user_blp
from .images import images_bp

def register_routes(application):
    application.register_blueprint(answers_blp)
    application.register_blueprint(choices_blp)
    application.register_blueprint(questions_blp)
    application.register_blueprint(stats_routes_blp)
    application.register_blueprint(user_blp)
    application.register_blueprint(images_bp)

