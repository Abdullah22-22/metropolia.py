import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            database="flight_game",
            user="root",
            password="12345",
            autocommit=True
        )
        return connection
    except mysql.connector.errors.InterfaceError:
        print("Cannot connect to DB")
        return None

@app.route("/airport/<icao_code>")
def get_airport(icao_code):
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "Cannot connect to database"}), 500

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code.upper(),))
    airport = cursor.fetchone()

    cursor.close()
    connection.close()

    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=3000)
