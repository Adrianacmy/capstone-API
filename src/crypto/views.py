import requests
import json

from django.shortcuts import render



# Create your views here.

def home(request):
  url_news = 'https://min-api.cryptocompare.com/data/v2/news/?lang=EN'
  news = json.loads(requests.get(url_news).content)

  url_price = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,LTC,XRP&tsyms=USD,EUR'
  price = json.loads(requests.get(url_price).content)

  context = {
    'news': news,
    'price': price
  }

  return render(request, 'home.html', context)

