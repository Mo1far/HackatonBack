from flask import jsonify


def success_response(data=None, status_code: int = 200):
    if data is None:
        return jsonify({'status': 'ok'}), status_code
    return jsonify({'status': 'ok',
                    **data}), 200


def error_response(msg: str, status_code: int):
    return jsonify({'status': 'error',
                    'msg': msg}), status_code
