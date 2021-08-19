from django.shortcuts import render
import requests
from .models import ApiApp


# Create your views here.
def home(request):
    responses = requests.get('https://restcountries.eu/rest/v2/all').json()

    context = {
        'response': responses
    }
    # for response in responses :
    #     ApiApp(
    #                 name = response["name"],
    #                 alpha2code = response["alpha2Code"],
    #                 alpha3code = response["alpha3Code"],
    #                 capital = response["capital"],
    #                 population = response["population"],
    #                 timezones = response["timezones"],
    #                 languages = response["languages"],
    #                 borders = response["borders"]
    #             ).save()

    return render(request, "apiApp/home.html", context)



# ApiApp(
    #         name = "test",
    #         alpha2code = "te",
    #         alpha3code = "te",
    #         capital = "test",
    #         population = 1,
    #         timezones = "test",
    #         languages = "test",
    #         borders = "test"
    #     ).save()