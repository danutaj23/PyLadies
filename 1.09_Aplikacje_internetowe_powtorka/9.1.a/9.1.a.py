# Napisz aplikację, która po wejściu na adres "/konto" wyświetli stan
# konta użytkownika i listę ostatnich przelewów. Początkowy stan konta
# ustaw np.na 1000 zł. Na stronie powinien znajdować się
# formularz, umożliwiający wykonanie przelewu - powinien zawierać dwa
# pola tekstowe: *nr konta docelowego, *kwotę przelewu.
# Po przesłaniu formularza kwota na koncie powinna zostać zmniejszona
# o podaną wartość, ponadto nowy przelew powinien pojawić się na liście
# ostatnich przelewów.
# Upewnij się, że odświeżenie strony po wykonaniu przelewu nie spowoduje
# wykonania tego przelewu jeszcze raz.


from flask import Flask, request, render_template, redirect

app = Flask(__name__)

saldo = 1000
przelewy = []


@app.route('/konto', methods=['GET', 'POST'])
def wykonanie_przelewu():
    global saldo
    if request.method == 'POST':
        numer_konta = request.form.get('numer_konta')
        kwota = int(request.form.get('kwota'))
        saldo -= kwota
        przelewy.append(
            {'numer_konta': numer_konta, 'kwota': kwota}
        )

        return redirect('/konto')

    return render_template('9.1.a.html', saldo=saldo, przelewy=przelewy)


app.run(debug=True)
