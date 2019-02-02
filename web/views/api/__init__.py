from flask import jsonify, request

from models.api_ip_whitelist import ApiIpWhitelist
from web.views.api import general
from web.views.blueprints import api_blueprint


@api_blueprint.before_request
def before_request():
    ip_address = request.remote_addr

    valid = ApiIpWhitelist.is_valid_ip(ip_address)

    if not valid:
        return send_response(error="IP is not whitelisted", status_code=403)


def send_response(data: dict = None, error: str = None, status_code: int = 200):
    """ All API endpoints must return this. """
    if data is None:
        data = {}

    response = {
        "data": data,
        "error": error,
    }

    return jsonify(response), status_code
