import requests


# Weather module
api_key = "TOKEN"
city = "Kiev"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)

json = request.json()

temp = json.get("main").get("temp")
temp_min = json.get("main").get("temp_min")
temp_max = json.get("main").get("temp_max")

print("Current temperature is", temp, "C")
print("Minimum temperature is", temp_min, "C")
print("Maximum temperature is", temp_max, "C")

# bot module

