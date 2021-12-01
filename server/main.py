from server import create_app
from .user.views import user_blueprint

app = create_app()


app.register_blueprint(user_blueprint, url_prefix="/auth")


@app.route("/", methods=["GET"])
def home():
    return {"message": "Server says Hi!!"}
