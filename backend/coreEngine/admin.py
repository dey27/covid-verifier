from django.contrib import admin

from .models import Initiative


class InitiativeAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Initiative._meta.fields] + ['label_list']
	list_filter = ['workforce_size', 'location_city', 'year_started', 'is_active']
	list_per_page = 20

	def get_queryset(self, request):
		"""
		Retrieves Labels for objects to minimize queries
		"""
		return super().get_queryset(request).prefetch_related('labels')

	@classmethod
	def label_list(cls, obj):
		"""
		Retrieves list of Labels for a given object.
		FuncName and FieldReferenceName from [list_display] should match.
		"""
		return u", ".join(o.name for o in obj.labels.all())

	class Meta:
		model = Initiative


admin.site.register(Initiative, InitiativeAdmin)
