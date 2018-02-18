import json

from flask import Blueprint, request

from models.api_ip_whitelist import ApiIpWhitelist

blueprint = Blueprint("api", __name__, url_prefix="/api")


@blueprint.before_request
def before_request():
    ip_address = request.remote_addr

    valid = ApiIpWhitelist.is_valid_ip(ip_address)

    if not valid:
        return send_response(error="IP is not whitelisted", status_code=403)


@blueprint.after_request
def api_after_request(response):
    response.headers["Content-Type"] = "application/json"
    return response


def send_response(data: dict = None, error: str = None, status_code: int = 200, sort_keys: bool = False):
    """ All API endpoints must return this. """
    if data is None:
        data = {}

    response = {
        "data": data,
        "error": error,
    }

    # We don't use jsonify here because Flask does not handle OrderedDict very well.
    return json.dumps(response, sort_keys=sort_keys), status_code


from . import general
