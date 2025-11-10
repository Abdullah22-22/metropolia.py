from flask import Flask, Response
import json

app = Flask(__name__)

def is_prime(n):
    if n <2:
        return False
    
    for i in range(2, int(n** 0.5) +1):
        if n % i== 0:   
            return False      
    return True

@app.route("/alkuluku/<Number>")

def get_alkuluku(Number):

    Number = int(Number)
    prime_result = is_prime(Number)

    result = {  
        "number" : Number,
        "isPrime": prime_result,
    }

    json_result= json.dumps(result)
    return Response(json_result, status=200, mimetype="application/json")



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)