from flask import Blueprint, request, jsonify
from .models import User, UserSchema
from ..helpers import APIResponse, protected, make_token

user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/signup", methods=["POST"])
def signup():
    user = UserSchema().load(request.json)
    user = User.upsert(user)
    user_response = UserSchema().dump(user)

    return APIResponse.respond(user_response)


@user_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.filter(User.username == data["username"]).first()
    if user and user.verify_password(data["password"]):
        return APIResponse.respond({"token": make_token(user)})
    return jsonify({"message": "No such user"}), 404


@user_blueprint.route("", methods=["GET"])
@protected
def get_user(user):
    return APIResponse.respond(UserSchema().dump(user))
