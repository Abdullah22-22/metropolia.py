import requests

API_KEY = "c6ef0aa0569d78b20b2e102fc3484d43"
city_name = input("Type city name: => ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_celsius = temp - 273.15

    print(f"Weather => {weather}, City => {city_name}")
    print(f"C° => {temp_celsius:.2f}")

else:
    print(f"Error fetching weather. Status code: {response.status_code}")
    print(response.json())
