from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
import pytz 

from django.utils import timezone

# Create your views here.







def index(request):
    
    cities = City.objects.all()
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5b36a0a06a9a0f09d5fe4b5f183b788d'

    if request.method == 'POST':
        
        form = CityForm(request.POST)
       
        form.save()
    
    form = CityForm()
    
    weather_data = []
    
    for city in cities:
        
        response = requests.get(url.format(city.name))
            
        if response.status_code == 404:
            
            continue 
        
        city_weather = response.json()
        
        weather = {
           
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'country': city_weather['sys']['country'],
            'sunrise': city_weather['sys']['sunrise'],
            'sunset': city_weather['sys']['sunset'],
            'windspeed': city_weather['wind']['speed']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'index.html', context)


def convert_to_localtime(utctime):
 
  fmt = '%d/%m/%Y %H:%M'
 
  utc = utctime.replace(tzinfo=pytz.UTC)
 
  localtz = utc.astimezone(timezone.get_current_timezone())

  return localtz.strftime(fmt)

#utcdate = convert_to_localtime(date_from_db)