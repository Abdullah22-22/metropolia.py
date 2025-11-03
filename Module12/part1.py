import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

if response.status_code == 200:
    data = response.json()
    joke = data.get ("value")

    print(f"joke ==> {joke}")

else:
    print("err in fetching  joke")


