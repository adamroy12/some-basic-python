import requests

# api key can be found on openweathermap.org

def get_weather_desc_and_temp():
    api_key = ""
    city = ""
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_max = json.get("main").get("temp_max")
    temp_min = json.get("main").get("temp_min")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max
            }

def main():
    weather_dict = get_weather_desc_and_temp()

    print("with low temperatures of", weather_dict.get('temp_min'))
    print("and high temperatures of", weather_dict.get('temp_max'))
    print("Today's forcast is "+ weather_dict.get('description'))

main()