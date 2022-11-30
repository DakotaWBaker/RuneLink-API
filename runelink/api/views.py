from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
# Create your views here.



# def get_ge_prices(request):
#   url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'
#   response = requests.get(url)
#   data = response.json()
#   return HttpResponse(json.dumps(data), content_type="application/json")

def get_ge_prices(request):
  url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'
  response = requests.get(url)
  data = response.json()
  return HttpResponse(json.dumps(data), content_type="application/json")

