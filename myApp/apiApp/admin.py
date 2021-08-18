from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ApiApp


class ApiAppAdmin(admin.ModelAdmin):
	list_display=('name', 'capital', 'population')
	search_fields=('name', 'capital')

	filter_horizontal=()
	list_filter=()
	fieldsets=()

admin.site.register(ApiApp, ApiAppAdmin)


# admin.site.register(ApiApp)
