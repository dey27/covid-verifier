from django.urls import path

from .views import *

app_name = 'coreEngine'

urlpatterns = [
	path(r'initiatives/', HomeView.as_view(), name='HomeView'),
]