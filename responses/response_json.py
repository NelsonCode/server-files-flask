from flask import jsonify, Response


def response_json(message: str, status: int = 200) -> Response:
    response = jsonify({
        "message": message
    })
    response.status_code = status
    return response
