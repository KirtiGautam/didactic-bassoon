from flask import request, Response, jsonify, make_response
from .config import SECRET, ALG
from .user.models import User
from functools import wraps
import jwt, datetime


def protected(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        try:
            token = request.headers["Authorization"].split()[1].strip()
            data = jwt.decode(token, SECRET, algorithms=ALG)
            user = User.get_by_id(data["id"])

        except Exception as ex:
            return jsonify({"message": "Invalid token"}), 401
        return func(user, *args, **kwargs)

    return decorated


def make_token(user: User) -> str:
    return jwt.encode(
        {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        },
        SECRET,
        algorithm=ALG,
    )


class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        return make_response(jsonify(data=data))
