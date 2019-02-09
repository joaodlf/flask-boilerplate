from flask import request

from models.api_ip_whitelist import ApiIpWhitelist
from web.views.api import general
from web.views.api.helpers import send_response
from web.views.blueprints import api_blueprint


@api_blueprint.before_request
def before_request():
    ip_address = request.remote_addr

    valid = ApiIpWhitelist.is_valid_ip(ip_address)

    if not valid:
        return send_response(error="IP is not whitelisted", status_code=403)
