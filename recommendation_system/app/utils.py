from flask import jsonify

def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code


def validate_user_id(user_id):
    if user_id is None or user_id == '':
        return False, 'user_id is required.'
    try:
        user_id = int(user_id)
        return True, user_id
    except ValueError:
        return False, 'user_id must be an integer.'
