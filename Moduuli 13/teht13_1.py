'''
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
'''
import json

from flask import Flask, Response

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = int(luku)

        jaollinen = 0

        for n in range(1, (luku + 1)):
            if luku % n == 0:
                jaollinen += 1

        if jaollinen == 2:
            prime = True
        else:
            prime = False

        tilakoodi = 200
        vastaus = {
            "number":luku,
            "isPrime":prime
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "Status":tilakoodi,
            "Virhe":"Virheellinen luku"
        }
    jsonvastaus = json.dumps(vastaus)
    return Response(jsonvastaus, tilakoodi, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status":404,
        "Virhe":"Virheellinen päätepiste"
    }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)