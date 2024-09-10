#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa
# lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
import mysql.connector
import geopy
from geopy import distance

def airport_coordinates(icao):
    sql = f'select latitude_deg, longitude_deg from airport where ident = "{icao}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    coordinate_data = cursor.fetchall()
    return coordinate_data


db_connection = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='flight_game',
         user='odeo',
         password='K4l4kukk0=!',
         autocommit=True
         )

icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")

airport1_co = airport_coordinates(icao1)
airport2_co = airport_coordinates(icao2)
print(f"{distance.distance(airport1_co,airport2_co).km:.2f} kilometriä")
