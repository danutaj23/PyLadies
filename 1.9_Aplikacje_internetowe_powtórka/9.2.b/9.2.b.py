# Do aplikacji dodaj stronę wyświetlającą wszystkie informacje o danym
# pracowniku. W ostatniej kolumnie tabeli z zadania 2a powinny
# pojawić się linki do stron z detalami poszczególnych użytkowników.
# Podpowiedź – w adresie strony z detalami przekaż identyfikator
# pracownika.

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
    return render_template("9.2.b_tabela.html", pracownicy=pracownicy)


@app.route('/szczegoly/<int:id>', methods=['GET'])
def szczegoly(id):
    filtr_pracownikow = []
    for pracownik in pracownicy:
        if pracownik.id == id:
            filtr_pracownikow.append(pracownik)
    pracownik = filtr_pracownikow[0]
    return render_template("9.2.b_szczegoly.html", pracownik=pracownik)


@app.route('/', methods=['GET'])
def przekierowanie():
    return redirect('pracownicy')


app.run(debug=True)
