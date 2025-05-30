

from flask import Blueprint, request, jsonify
from app.models.recommender import Recommender
from app.utils import error_response, validate_user_id

recommender = Recommender()
bp = Blueprint('recommendations', __name__)

@bp.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    valid, result = validate_user_id(user_id)
    if not valid:
        return error_response(result, 400)
    user_id = result
    recommendations = recommender.recommend(user_id)
    if not recommendations:
        return error_response('No recommendations found for this user or user does not exist.', 404)
    return jsonify({'user_id': user_id, 'recommendations': recommendations})
