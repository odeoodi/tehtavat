#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja
# tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

def get_airport_by_icao(icao):
    sql = f"select name, municipality from airport where ident = '{icao}'"
    #print(sql)
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

db_connection = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='flight_game',
         user='odeo',
         password='K4l4kukk0=!',
         autocommit=True
         )

icao = input("Anna ICAO-koodi: ")
airport = get_airport_by_icao(icao)
print(f'{airport[0][0]}, {airport[0][1]}')


