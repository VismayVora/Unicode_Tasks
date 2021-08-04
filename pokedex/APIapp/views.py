from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponse
from django.http import JsonResponse
import json

#def index(request):
     #return HttpResponse("<h1>Trying to implement Pokedex Task</h1>")

def index(request):
     r = requests.get('https://pokeapi.co/api/v2/type/')
     if r.status_code == 200:
          return HttpResponse('Yay! It worked!\n{}'.format(r.text))


#def index(request):
#     r = requests.get('https://pokeapi.co/api/v2/type/')
#     if r.status_code == 200:
#        return JsonResponse(r.text, safe=False)
