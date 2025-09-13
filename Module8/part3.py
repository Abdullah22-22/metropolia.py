from db import get_connection
from geopy.distance import geodesic

conn = get_connection()
cursor = conn.cursor()

icao1 = input("Anna koti  lentokentän ICAO-koodi: ")
icao2 = input("Anna tie  lentokentän ICAO-koodi: ")

cursor.execute(
    "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
    (icao1,)
)
result1 = cursor.fetchone()

cursor.execute(
    "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
    (icao2,)
)
result2 = cursor.fetchone()

if result1 and result2:
    coords1 = (result1[0], result1[1])
    coords2 = (result2[0], result2[1])
    distance_km = geodesic(coords1, coords2).kilometers
    print(f"etäisyys on {distance_km:.2f} KM")

else:
    print("Jokin lentokentistä ei löytynyt tietokannasta.")

cursor.close()
conn.close()
