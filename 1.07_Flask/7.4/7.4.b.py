# ...jeśli użytkownik poda nieistniejącą planetę,
# powinien otrzymać komunikat
# "Planet <nazwa_planety> does not exist".

import json
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/planet-details", methods=["GET", "POST"])
def planet_details():
    planet = request.args["planet"]
    swapi_resp = requests.get(
        "https://swapi.co/api/planets/?search=" + planet
         )
    planets = swapi_resp.json()["results"]
    if not planets:
        return "Planet {} does not exist".format(planet)

    planet_data = planets[0]
    response = {"klimat": planet_data["climate"],
                "liczba mieszkancow": planet_data["population"]}
    return json.dumps(response)


app.run(debug=True)
