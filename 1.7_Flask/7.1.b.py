# (Do domu) Powyższy program zabezpiecz przed sytuacją,
# w której użytkownik poda ciąg znaków zamiast liczby.
# [http://flask.pocoo.org/docs/0.12/quickstart/#variable-rules]

from flask import Flask

app = Flask(__name__)


@app.route("/add/<int:liczba1>/<int:liczba2>")
def dodawanie(liczba1, liczba2):
    return "{}".format(liczba1 + liczba2)


app.run(debug=True)


# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/add/<liczba1>/<liczba2>")
# def dodawanie(liczba1, liczba2):
#     try:
#         wynik = int(liczba1) + int(liczba2)
#         if type(wynik) is int:
#             return "{}".format(wynik)
#     except ValueError:
#         return "Podaj dwie liczby całkowite."
#
#
# app.run(debug=True)
