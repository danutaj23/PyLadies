# Napisz program, który: po wejściu na adres
# /user/<username>/set-password ustawi hasło użytkownika
# username (na podstawie podanego JSON-a).

from flask import Flask, request

app = Flask(__name__)
user_dict = {}


@app.route("/user/<username>/set-password", methods=["POST"])
def set_password(username):
    data = request.get_json()
    user_password = data["password"]
    user_dict[username] = user_password
    return "Hasło użytkownika {} to: {}".format(username, user_password)


app.run(debug=True)







