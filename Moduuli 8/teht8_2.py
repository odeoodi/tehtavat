#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa
# olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector


def get_airport_types_by_iso_country(iso_country):
    sql = f"select type, count(*) from airport where iso_country = '{iso_country}' group by type"
    #print(sql)
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(sql)
    airport_type_data = cursor.fetchall()
    return airport_type_data

db_connection = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='flight_game',
         user='odeo',
         password='K4l4kukk0=!',
         autocommit=True
         )
maakoodi = input("Anna maakoodi: ")
airport_types = get_airport_types_by_iso_country(maakoodi)
for airport in airport_types:
    print(f'{airport["type"]} ja {airport["count(*)"]}')

