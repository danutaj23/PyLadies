# Napisz program, który po wejściu na adres /current-status
# metodą POST ustawi aktualny status na podstawie przekazanego
# w zapytaniu JSON-a (np. {"status": "starting"}), a po wejściu
# na ten sam adres metodą GET zwróci aktualny status.

from flask import Flask, request

app = Flask(__name__)

saved_status = "unknown"


@app.route("/current-status", methods=["GET", "POST"])
def save_status():
    if request.method == "POST":
        global saved_status
        data = request.get_json()
        saved_status = data["status"]
        return "Status: {}".format(data["status"])
    else:
        return saved_status


app.run(debug=True)


