from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]
    list_filter = ['is_processed']
    list_per_page = 20

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
