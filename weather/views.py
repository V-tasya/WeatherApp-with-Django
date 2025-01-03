import requests # is used for post and get requests
from django.shortcuts import render

#this function is processing requests on a home page of an app
def index(request):
    appid = 'c3efdac01664d4464d1f614b2a2ec6fa'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metrics&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json() # method get sends get-request, format is used for substitution values into {}, json() converts json format into a dictionary

    #for getting info from the set(city, temperature, weather item)
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'item': res["weather"][0]["icon"]
    }

    context = {
        'info': city_info
    }
    #print(res.text)

    return render(request, 'weather/index.html', context)
