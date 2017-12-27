# Napisz program, który po wejściu na adres /hello
# odpowie dowolnym komunikatem powitalnym
# (np. "Hello world!"), a po wejściu na adres /witam
# zwróci przekierowanie na adres /hello.
# Działanie programu sprawdź w przeglądarce.
# [http://flask.pocoo.org/docs/0.12/quickstart/#redirects-and-errors]

from flask import Flask, redirect

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Cześć!"


@app.route("/witam")
def witam():
    return redirect("/hello")


app.run(debug=True)


