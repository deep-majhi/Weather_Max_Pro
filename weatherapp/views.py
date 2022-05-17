from django.shortcuts import render
import requests
import datetime

import urllib.request
import json
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=5e5b6f8599e98392d194be1e8af8c5c3').read()
        api_url2 = json.loads(api_url)

        data = {
            "country": city,
            "weather_description": api_url2['weather'][0]['description'],
            "weather_temperature": api_url2['main']['temp'],
            "weather_icon": api_url2['weather'][0]['icon'],
            "weather_temperature_min": api_url2['main']['temp_min'],
            "weather_temperature_max": api_url2['main']['temp_max'],
            "weather_pressure": api_url2['main']['pressure'],
            "weather_country": api_url2['sys']['country'],
            
        }
        day = datetime.date.today()
        
    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_icon": None,
            "weather_temperature_min": None,
            "weather_temperature_max": None,
            "weather_pressure":None,
            "weather_country":None,
        }
        day = datetime.date.today()
    print(data['weather_icon'])
    return render(request, 'weatherapp/index.html', {"city": city, "data" :data , "day":day})