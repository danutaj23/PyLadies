# Napisz program, który po wejściu na adres /planet-details?planet=Tatooine
# odpowie jsonem zawierającym dane planety, o którą zapytał użytkownik
# (np. klimat, liczba mieszkańców). Dane planety program powinien pobierać
# ze Star Wars API, np.: https://swapi.co/api/planets/?search=Tatooine

import json
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/planet-details", methods=["GET", "POST"])
def planet_details():
    swapi_resp = requests.get(
        "https://swapi.co/api/planets/?search=Tatooine"
         )
    planets = swapi_resp.json()["results"]

    planet_data = planets[0]
    response = {"klimat": planet_data["climate"],
                "liczba mieszkancow": planet_data["population"]}
    return json.dumps(response)


app.run(debug=True)
