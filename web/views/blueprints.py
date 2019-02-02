from flask import Blueprint

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

public_blueprint = Blueprint("public", __name__)
