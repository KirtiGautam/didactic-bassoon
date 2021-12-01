from flask import Blueprint, request
from .models import User, UserSchema
from ..helpers import APIResponse

user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/signup", methods=["POST"])
def signup():
    user = UserSchema().load(request.json)
    user = User.upsert(user)
    user_response = UserSchema().dump(user)

    return APIResponse.respond(user_response)
