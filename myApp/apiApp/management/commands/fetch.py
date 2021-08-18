from django.core.management.base import BaseCommand
import django
import os
import requests
from apiApp import models


class Command(BaseCommand):
    help = 'Fetch Data From API.'

    def handle(self, *args, **kwargs):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myApp.settings")

        django.setup()

        response = requests.get('https://restcountries.eu/rest/v2/all').json()

        for data in response:
            try:
                table = models.ApiApp()
                table.name = data.get('name')
                table.alpha2code = data.get('alpha2code')
                table.alpha3code = data.get('alpha3code')
                table.capital = data.get('capital')
                table.population = data.get('population')
                table.timezones = data.get('timezones')
                table.languages = data.get('languages')
                table.borders = data.get('borders')
                table.save()

                print("Please Wait...")
            except Exception as ex:
                print(ex)
            # print("Could Not Save: ", data.get('name'))

        self.stdout.write("Action Completed!")
