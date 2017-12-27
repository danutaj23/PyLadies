# (Do domu) ...po wejściu na /user/<username>/login
# aplikacja powinna zwracać token w formacie UUID4.
# [https://docs.python.org/3.6/library/uuid.html]

from flask import Flask, request
import uuid

app = Flask(__name__)
user_dict = {}


@app.route("/user/<username>/set-password", methods=["POST"])
def set_password(username):
    data = request.get_json()
    user_password = data["password"]
    user_dict[username] = user_password
    return "Hasło użytkownika {} to: {}".format(username, user_password)


@app.route("/user/<username>/login", methods=["POST"])
def login(username):
    password = request.get_json()["password"]
    if username in user_dict:
        if password == user_dict[username]:
            return str(uuid.uuid4())
        else:
            return "Wrong password"
    else:
        return "Wrong login or password"


app.run(debug=True)
