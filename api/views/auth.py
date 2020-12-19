from flask import request, jsonify
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required

from api.app import db
from api.models.user import User
from api.views import auth_bp
from api.views.utils import success_response


@auth_bp.route('login/', methods=['POST'])
def login():
    if not request.is_json:
        return success_response(dict(error=dict(message="Missing JSON in request")), 400)

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return success_response(dict(error=dict(message="Missing username parameter")), 400)
    if not password:
        return success_response(dict(error=dict(message="Missing password parameter")), 400)

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify(dict(error=dict(message="User not found"))), 404

    if not user or not check_password_hash(user.password, password):
        return success_response(dict(error=dict(message="Bad username or password")), 401)

    # Identity can be any data that is json serializable
    access_token = create_access_token(
        identity=dict(
            user_id=user.id,
            name=user.user_name,
        ))
    return success_response(dict(access_token=access_token), 200)


@auth_bp.route('signup/', methods=['POST'])
def signup():
    # creates a dictionary of the form data
    data = request.json

    # gets name, email and password
    user_name = data.get('user_name')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')

    # checking for existing user
    user = User.query \
        .filter_by(email=email) \
        .first()
    if not user:
        # database ORM object
        user = User()
        user.user_name = user_name
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.password = generate_password_hash(password)

        # insert user
        db.session.add(user)
        db.session.commit()

        return success_response(dict(message="Successfully registered"), 201)
    else:
        # returns 202 if user already exists
        return success_response(dict(message="User already exists. Please Log in"), 202)


@auth_bp.route('profile/<int:id>/', methods=['GET'])
@jwt_required
def profile(id=None):
    user = User.query.filter(User.id == id).first()
    return success_response(user.serialize_short())
