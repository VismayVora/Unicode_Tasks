from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponse

def index(request):
     #title = "Pokemon Types"
     r = requests.get('https://pokeapi.co/api/v2/type/')
     if r.status_code == 200:
          return HttpResponse(r)
          #types = HttpResponse(r)
          #return render(request, 'base.html', {'title': title, 'types': types})
