from django.contrib import admin

from .models import Initiative

class InitiativeAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Initiative._meta.fields]
	list_per_page = 20

	class Meta:
		model = Initiative

admin.site.register(Initiative, InitiativeAdmin)