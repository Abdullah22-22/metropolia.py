from db import get_connection


conn = get_connection()
cursor = conn.cursor()

valittu= input("anna  maakoodi : =>  ")
sql= """
        SELECT type,COUNT(*)
        FROM airport
        WHERE iso_country =%s
        GROUP BY type
     """

cursor.execute(sql,(valittu ,))
results = cursor.fetchall()

if results:
    print(f" lentokentät maa {valittu}")
    for airport_type , count in results:
        print((f"{airport_type} :=> {count}"))
else:
    print("maa koodi on virhe")

cursor.close()
conn.close()
