from server import app


@app.route("/", methods=["GET"])
def home():
    return {"message": "Server says Hi!!"}
