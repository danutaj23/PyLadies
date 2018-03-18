from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get('name', '')
    return render_template('8.3.html', query=name)


app.run(debug=True)


# Uruchom aplikację, sprawdź w przeglądarce:
# http://127.0.0.1:5000/hello?name=JakieśImię
