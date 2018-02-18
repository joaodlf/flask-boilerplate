from . import blueprint, send_response


@blueprint.route("/general/ping", methods=["GET"])
def general_ping():
    """ Just a ping/pong to determine if this web server is up and running. """
    return send_response(data={"ping": "pong"})
