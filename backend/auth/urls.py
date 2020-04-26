from django.urls import path
from django.conf.urls import url, include
from .views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
