from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/search", methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    return render_template('8.5.html', query=query)


app.run(debug=True)


# Uruchom aplikację, sprawdź w przeglądarce:
# http://127.0.0.1:5000/search
