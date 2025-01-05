# in django views.py is suitable for processing requests and returning answers
# how app well react on a definite client's request
import requests # is used for post and get requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

#this function is processing requests on a home page of an app
def index(request):
    appid = 'c3efdac01664d4464d1f614b2a2ec6fa'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metrics&appid=' + appid

    # if send method equals to post
    if(request.method == 'POST'):
        form = CityForm(request.POST) # request.POST contains data sent threw the form, this date transmitted for processing into a CityForm
        form.save() # saves data from the form in database

    form = CityForm() # for clearing the form

    cities = City.objects.all() # choosing all data from the tab(all cities)

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()  # method get sends get-request, format is used for substitution values into {}, json() converts json format into a dictionary
        # for getting info from the set(city, temperature, weather item)
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'item': res["weather"][0]["icon"]
        }
        # writing all city's data in a list
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }
    #print(res.text)

    return render(request, 'weather/index.html', context)
