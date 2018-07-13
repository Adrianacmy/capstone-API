import requests
import json

from django.shortcuts import render



# Create your views here.

def home(request):
  url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=EN'
  news = json.loads(requests.get(url).content)
  return render(request, 'home.html', {'news': news})