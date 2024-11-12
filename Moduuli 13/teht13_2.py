'''
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin
JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava
 GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
 {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
'''
import json

from flask import Flask, Response, request

import mysql.connector

app = Flask(__name__)
@app.route('/airport/<icao>')
def airport(icao):
    try:
        def get_airport(icaocode):
            sql = f"select name,municipality from airport where ident = '{icaocode}'"
            cursor = db_connection.cursor()
            cursor.execute(sql)
            airport_data = cursor.fetchone()
            return airport_data

        db_connection = mysql.connector.connect(
            host='127.0.0.1',  # host='localhost'
            port=3306,
            database='flight_game',
            user='odeo',
            password='K4l4kukk0=!',
            autocommit=True
        )

        airport_data = get_airport(icao)
        if airport_data:
            name = airport_data[0]
            municipality = airport_data[1]
            statuscode = 200
            answer = {
                "Name":name,
                "Municipality":municipality,
                "ICAO":icao
            }
        else:
            statuscode = 400
            answer = {
                "status": statuscode,
                "text": f"Incorrect ICAO code, you wrote '{icao}'"
            }
    except mysql.connector.Error as err:
        statuscode = 500
        answer = {
            "status": statuscode,
            "text": f"Database error: {err}"
        }
    finally:
        db_connection.close()

    jsonanswer = json.dumps(answer)
    return Response(response=jsonanswer, status=statuscode, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(error):
    answer = {
        "status":404,
        "text":"Mistake in the URL"
    }
    jsonanswer = json.dumps(answer)
    return Response(response=jsonanswer, status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader = True, host='127.0.0.1', port=3000)



