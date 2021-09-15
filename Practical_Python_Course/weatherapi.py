import requests


api_key = "5c25ce202c92197962e98ad9e48d5fa4"
city = "Newcastle upon Tyne"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today's forcast is "+description)

temp_min = json.get("main").get("temp_min")
print("with low temperatures of", temp_min)

temp_max = json.get("main").get("temp_max")
print("and high temperatures of", temp_max)