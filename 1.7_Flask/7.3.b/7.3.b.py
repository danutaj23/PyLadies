# ...po wejściu na /user/<username>/login odpowie komunikatem
# "Login successful" jeśli podane w JSON-ie hasło zgadza się
# z wcześniej ustawionym lub – jeśli hasło się nie zgadza
# albo w ogóle nie zostało ustawione – komunikatem
# "Wrong password".

from flask import Flask, request

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
            return "Login successful"
        else:
            return "Wrong password"
    else:
        return "Wrong login or password"


app.run(debug=True)
