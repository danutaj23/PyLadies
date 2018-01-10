# Aplikację z punktu 1a. zmodyfikuj tak, aby po wejściu na adres "/"
# użytkownik został przekierowany na adres "/konto".


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

    return render_template('9.1.b.html', saldo=saldo, przelewy=przelewy)


@app.route('/')
def przekierowanie():
    return redirect('/konto')


app.run(debug=True)
