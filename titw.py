import os
import random

from flask import abort, Flask, jsonify, request


app = Flask(__name__)


gif_urls = [
    "https://i.imgur.com/c72ls2T.gif",
    "https://i.imgur.com/Fk69QjI.gif",
    "https://media1.tenor.com/images/22986bd8be9bf3611e6f449ad67ecd75/tenor.gif?itemid=16169913",
    "https://media1.tenor.com/images/df5620680add36f8561b05e7b26bb58c/tenor.gif?itemid=15639949",
    "https://media1.tenor.com/images/614de537ea516c274f9c95e722fbf9d5/tenor.gif?itemid=15630699"
]


def request_valid(request):
    token = request.form["token"] == os.environ["SLACK_VERIFICATION_TOKEN"]
    team_id = request.form["token"] == os.environ["SLACK_TEAM_ID"]

    return token and team_id


@app.route("/titw", methods=["POST"])
def titw():
    if not request_valid:
        abort(400)

    gif_url = random.choice(gif_urls) 

    return jsonify(response_type="in_channel", text=f"<{gif_url}|This is the way.>")

