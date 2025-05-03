from flask import Blueprint

bp = Blueprint('content', __name__, url_prefix='/bell')

def initialize_routes(app):
    from . import bell
    app.register_blueprint(bp)