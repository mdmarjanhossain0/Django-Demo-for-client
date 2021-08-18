from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    response = requests.get('https://restcountries.eu/rest/v2/all').json()
    context = {
        'response': response
    }
    return render(request, "apiApp/home.html", context)
