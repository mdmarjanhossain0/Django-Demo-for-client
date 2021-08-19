from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from apiApp.models import ApiApp
from apiApp.api.serializers import CountrySerializer, CountryUpdateSerializer, CountryCreateSerializer
SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Urls: 
		# 1) http://127.0.0.1:8000/api/country/list 
		# 2) list: http://127.0.0.1:8000/api/country/list
		# 3) pagination: http://127.0.0.1:8000/api/country/list?page=2
		# 4) search: http://<your-domain>/api/blog/list?search=Bangladesh 
		# 5) search + pagination + ordering: http://127.0.0.1:8000/api/country/list?search=Bangladesh&page=1

		# Search Fields: (country, capital, population, languages, borders)
class ApiCountryListView(ListAPIView):
	queryset = ApiApp.objects.all()
	serializer_class = CountrySerializer
	pagination_class = PageNumberPagination
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('name', 'capital', 'population', 'languages', 'borders')


# Url: http://127.0.0.1:8000/api/country/<country_name>/update

@api_view(['PUT'])
def api_update_country_view(request, country_name):

	print(request.data)
	try:
		country = ApiApp.objects.get(name=country_name)
	except ApiApp.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'PUT':
		print(request.data)
		serializer = CountryUpdateSerializer(country, data=request.data, partial=True)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['response'] = UPDATE_SUCCESS
			data['name'] = country.name
			data['alpha2code'] = country.alpha2code
			data['alpha3code'] = country.alpha3code
			data['capital'] = country.capital
			data['population'] = country.population
			data['timezones'] = country.timezones
			data['languages'] = country.languages
			data['borders'] = country.borders
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Url: http://127.0.0.1:8000/api/country/create
@api_view(['POST'])
def api_create_country_view(request):

	if request.method == 'POST':
		data = request.data
		print(data)
		serializer = CountryCreateSerializer(data=data)

		data = {}
		if serializer.is_valid():
			country = serializer.save()
			data['response'] = CREATE_SUCCESS
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  http://127.0.0.1:8000/api/country/<country_name>/delete
@api_view(['DELETE'])
def api_delete_country_view(request, country_name):

	try:
		country = ApiApp.objects.get(name=country_name)
	except ApiApp.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'DELETE':
		operation = country.delete()
		data = {}
		if operation:
			data['response'] = DELETE_SUCCESS
		return Response(data=data)