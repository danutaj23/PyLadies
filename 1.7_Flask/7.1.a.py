# Napisz program, który po wejściu na adres:
# /add/<liczba1>/<liczba2> odpowie sumą podanych liczb.
# Przykład: wejście na /add/3/5 powinno zwrócić "8".

from flask import Flask

app = Flask(__name__)


@app.route("/add/<liczba1>/<liczba2>")
def dodawanie(liczba1, liczba2):
    wynik = int(liczba1) + int(liczba2)
    return "{}".format(wynik)


app.run(debug=True)


