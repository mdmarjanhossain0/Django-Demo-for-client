from django.urls import path

from apiApp.api.views import(
    ApiCountryListView,
    api_update_country_view,
    api_create_country_view,
    api_delete_country_view
)

app_name = "country_api"

urlpatterns = [
    path("list", ApiCountryListView().as_view(), name="list"),
    path("<country_name>/update", api_update_country_view, name="update"),
    path("create", api_create_country_view, name="create"),
    path("<country_name>/delete", api_delete_country_view, name="delete")
]
