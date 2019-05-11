from flask import jsonify


def send_response(data: dict = None, error: str = None, status_code: int = 200):
    """ All API endpoints must return this. """
    if data is None:
        data = {}

    response = {"data": data, "error": error}

    return jsonify(response), status_code
