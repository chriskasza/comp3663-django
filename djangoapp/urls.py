"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoapp import weather 

from django.http import HttpResponse
import requests

def currentWeather(request):
    result = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Wolfville,ca&APPID=1c612550bab05b2d74696169c71bdc84')
    w = weather.Weather(result.json())
    return HttpResponse(w.jsonResp())

# http://localhost:8000/historicalWeather?year=1940
def historicalWeather(request):
    year = request.GET.get('year')
    return HttpResponse('')
    
urlpatterns = [
    path('weather', currentWeather),
    path('historicalWeather', historicalWeather),
]
