from db import get_connection


conn = get_connection()
cursor = conn.cursor()

valittu= input("anna Lentokenttä: =>  ")
cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (valittu,))

result = cursor.fetchone()
if result:
    print(f"Lentokenttä nimi {result[0]}, kaupunki {result[1]}")

else:
    print("ei ole Lentokenttä ")


cursor.close()
conn.close()