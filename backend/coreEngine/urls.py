from django.urls import path

from .views import *

app_name = 'coreEngine'

urlpatterns = [
    path(r'search_values/', SearchBarValuesView.as_view(), name='SearchBarValuesView'),
    path(r'posts/', PostsView.as_view(), name='PostsView'),
    path(r'votes/', VotesView.as_view(), name='VotesView'),
]
