import mysql.connector



def get_airport_by_icao(icao):
    sql = f"select name, municipality from airport where ident = '{icao}'"
    #print(sql)
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    #nämä kolme yllä on samat aina, voi käyttää pohjana
    return airport_data

def get_airports_by_municipality(municipality):
    sql = f"select ident, name from airport where municipality = '{municipality}'"
    # print(sql)
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

def get_airportsi_by_municipality(municipality):
    sql = f"select ident, name, elevation_ft,type from airport where municipality = '{municipality}'"
    # print(sql)
    cursor = db_connection.cursor(dictionary=True)
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

#icao = input("Anna lentokentän ICAO-koodi: ")
#airport = get_airport_by_icao("efhs")

#print(get_airports_by_municipality("Helsinki"))

airports = get_airportsi_by_municipality("Helsinki")
print(airports)
for airport in airports:
    print(f"{airport['ident']} nimi on {airport['name']}, tyyppi on {airport['type']}  ja korkeus on {airport['elevation_ft']}ft")


'''
print(airport)
print(airport[0])
print(airport[0][0])
print(airport[0][1])


tulostaa:
[('Seinäjoen Central Hospital Heliport', 'Seinäjoen')]
('Seinäjoen Central Hospital Heliport', 'Seinäjoen')
Seinäjoen Central Hospital Heliport
Seinäjoen
'''