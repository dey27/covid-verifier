from django.urls import path

from .views import *

app_name = 'AIEngine'

urlpatterns = [
    path(r'populate-db/', PopulateDBView.as_view(), name='PopulateDBView'),
    path(r'articles/', ArticleView.as_view(), name='ArticleView'),
]
