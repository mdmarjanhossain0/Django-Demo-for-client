from django.core.management.base import BaseCommand
import django
import os
import requests
from apiApp.models import ApiApp


class Command(BaseCommand):
    help = 'Fetch Data From API.'

    def handle(self, *args, **kwargs):
        # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myApp.settings")

        # django.setup()

        responses = requests.get('https://restcountries.eu/rest/v2/all').json()

        for response in responses:
            try:
                ApiApp(
                    name = response["name"],
                    alpha2code = response["alpha2Code"],
                    alpha3code = response["alpha3Code"],
                    capital = response["capital"],
                    population = response["population"],
                    timezones = response["timezones"],
                    languages = response["languages"],
                    borders = response["borders"]
                ).save()
                print("Please Wait...")
            except Exception as ex:
                print(ex)


        self.stdout.write("Action Completed!")




# for data in response:
        #     try:
        #         table = models.ApiApp()
        #         table.name = data.get('name')
        #         table.alpha2code = data.get('alpha2code')
        #         table.alpha3code = data.get('alpha3code')
        #         table.capital = data.get('capital')
        #         table.population = data.get('population')
        #         table.timezones = data.get('timezones')
        #         table.languages = data.get('languages')
        #         table.borders = data.get('borders')
        #         table.save()

        #         print("Please Wait...")
        #     except Exception as ex:
        #         print(ex)
        #     # print("Could Not Save: ", data.get('name'))
