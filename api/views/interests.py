from flask import jsonify, request
from flask_jwt_extended import jwt_required

from api.app import db
from api.models.interest import Interest
from api.models.user import User
from api.views import interests_bp
from api.views.utils import success_response, error_response


@interests_bp.route('/', methods=['GET'])
@jwt_required
def interests_list():
    interests = Interest.query.all()
    return success_response(data=[interest.serialize_short() for interest in interests])


@interests_bp.route('add_to_user/', methods=['POST'])
@jwt_required
def add_interest_to_user():
    data = request.json
    user_id = data['user_id']
    interests_ids = data['interests_ids']
    user = User.query.filter(User.id == user_id).first()
    user_interests_ids = [interest.id for interest in user.interests]
    for interest_id in interests_ids:
        if interest_id not in user_interests_ids:
            new_interest = Interest.query.filter(Interest.id == interest_id).first()
            if new_interest is None:
                return error_response(f'Interest id - {interest_id} didnt exist', 404)
            user.interests.append(new_interest)
    db.session.add(user)
    db.session.commit()
    return success_response(user.serialize_short())
