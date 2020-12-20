from operator import or_

from flask import request
from flask_jwt_extended import get_jwt_identity
from sqlalchemy import select, and_

from api.app import db
from api.models.user import User, user_friendship, FriendshipStatus, Friendship
from api.views import friends_bp
from api.views.utils import success_response, error_response


@friends_bp.route('add_friend/<int:target_user_id>/', methods=['POST'])
def add_friend(target_user_id):
    current_user_id = get_jwt_identity()['user_id']

    if current_user_id == target_user_id:
        return error_response('You cannot add yourself as a friend', 400)

    current_user = User.query.filter(User.id == current_user_id).first()
    target_user = User.query.filter(User.id == target_user_id).first()

    if target_user_id is None:
        return error_response(f'User with id {target_user_id} not found', 400)

    if target_user not in current_user.friends:
        current_user.friends.append(target_user)
    else:
        return error_response('User already you friend', 200)

    db.session.add(current_user)
    db.session.commit()

    return success_response()


@friends_bp.route('add_best_friend/', methods=['POST'])
def add_best_friend():
    data = request.form
    current_user = User.query.filter(User.id == data['current_user']).first()
    target_user = User.query.filter(User.id == data['target_user']).first()

    new_friendship = Friendship()
    new_friendship.requester_id = current_user.id
    new_friendship.target_id = target_user.id

    current_user.friendship.append(new_friendship)
    target_user.friendship.append(new_friendship)

    db.session.add(current_user, target_user)
    db.session.commit()
    return success_response()


@friends_bp.route('/')
def friendships_list():
    data = request.json
    user_id = data['user_id']
    user = User.query.filter(User.id == user_id).first()
    friendships = Friendship.query.filter(or_(
        Friendship.requester_id == user.id, and_(Friendship.target_id == user_id,
                                                 Friendship.status == FriendshipStatus.accepted_second_level))).all()

    return success_response({'friends': [friendship.serialize_short() for friendship in friendships]})


@friends_bp.route('accept_friend/', methods=['POST'])
def accept_friendship():
    data = request.form
    current_user_id = data['current_user_id']
    requester_id = data['target_user_id']

    current_user = User.query.filter(User.id == current_user_id).first()
    requester_user = User.query.filter(User.id == requester_id).first()

    user_friendship_record = Friendship.query.filter(Friendship.requester_id == requester_user.id,
                                                     Friendship.target_id == current_user.id,
                                                     FriendshipStatus == FriendshipStatus.requested).first()

    user_friendship_record.status = FriendshipStatus.accepted_second_level
    db.session.add(user_friendship_record)
    db.session.commit()

    return success_response()
