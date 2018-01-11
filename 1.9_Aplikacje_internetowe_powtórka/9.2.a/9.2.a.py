# Napisz aplikację, która będzie wyświetlać dane pracowników pewnej
# firmy. Każdy pracownik będzie mieć identyfikator, imię, nazwisko,
# płacę, opis stanowiska (użyj klasy po stronie serwera).
# Utwórz stonę zawierającą tabelę pracowników (adres wymyśl
# samodzielnie). W każdym wierszu tabeli powinny znaleźć się
# imię, nazwisko pracownika i dodatkowa pusta komórka
# - uzupełnimy ją w następnym zadaniu.

from flask import Flask, render_template, redirect

app = Flask(__name__)

class Pracownik:
    def __init__(self, id, imie, nazwisko, placa, opis_stanowiska):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.placa = placa
        self.opis_stanowiska = opis_stanowiska


pracownicy = [
    Pracownik(1, "Jan", "Kowalski", 3000, "Kierowca bombowca"),
    Pracownik(2, "Anna", "Kowalska", 12500, "Kreatywna księgowa"),
    Pracownik(3, "Kazimierz", "Nowak", 4555, "Wizażysta zwłok"),
    Pracownik(4, "Hanna", "Iksińska", 5333, "Asystentka prezesa")
]


@app.route('/pracownicy', methods=['GET'])
def tabela():
    return render_template("9.2.a_tabela.html", pracownicy=pracownicy)


@app.route('/', methods=['GET'])
def przekierowanie():
    return redirect('pracownicy')


app.run(debug=True)
