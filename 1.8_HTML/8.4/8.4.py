# Utwórz klasę Osoba. Każda instancja tej klasy powinna posiadać
# trzy atrybuty – imię, nazwisko i wiek.
# Utwórz listę kilku dowolnych osób.
# Utwórz szablon HTML, który będzie renderował tabelę osób
# (imię, nazwisko i wiek powinny wyświetlać się w osobnych kolumnach).
# Napisz program, który po wejściu na adres /osoby renderuje ten szablon.
# Przetestuj program w przeglądarce.

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/osoby")
def tabela():
    osoby = []

    class Osoba:
        def __init__(self, imie, nazwisko, wiek):
            self.imie = imie
            self.nazwisko = nazwisko
            self.wiek = wiek
            osoby.append(self)

    Osoba("Jan", "Kowalski", 30)
    Osoba("Anna", "Kowalska", 20)
    Osoba("Kazimierz", "Nowak", 55)
    Osoba("Hanna", "Iksińska", 33)

    return render_template("8.4.html", list=osoby)


app.run(debug=True)
