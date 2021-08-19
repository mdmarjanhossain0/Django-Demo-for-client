from rest_framework import serializers
from apiApp.models import ApiApp



class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiApp
        fields = [
            'name',
            'alpha2code',
            'alpha3code',
            'capital',
            'population',
            'timezones',
            'languages',
            "borders"
        ]


class CountryUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = ApiApp
		fields = ['name', 'capital', 'population']

	def validate(self, country):
		try:
			name = country['name']
			capital = country['capital']
			population = country['population']
		except KeyError:
			pass
		return country


class CountryCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = ApiApp
		fields = [
            'name',
            'alpha2code',
            'alpha3code',
            'capital',
            'population',
            'timezones',
            'languages',
            "borders"
        ]

	def save(self):
		try:
			name = self.validated_data['name']
			alpha2code = self.validated_data['alpha2code']
			alpha3code = self.validated_data['alpha3code']
			capital = self.validated_data['capital']
			population = self.validated_data['population']
			timezones = self.validated_data['timezones']
			languages = self.validated_data['languages']
			borders = self.validated_data['borders']
		
			country = ApiApp(
				name = name,
				alpha2code = alpha2code,
				alpha3code = alpha3code,
				capital = capital,
				population = population,
				timezones = timezones,
				languages = languages,
				borders = borders
			)

			country.save()
			return country
		except KeyError:
			raise serializers.ValidationError({"response": "Some Error."})
