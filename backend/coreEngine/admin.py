from django.contrib import admin

from .models import Posts, Votes


class PostsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Posts._meta.fields] + ['label_list']
    list_filter = ['location_city']
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
        model = Posts


admin.site.register(Posts, PostsAdmin)


class VotesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Votes._meta.fields]
    list_per_page = 20

    class Meta:
        model = Votes


admin.site.register(Votes, VotesAdmin)
