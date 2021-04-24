from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.conf import settings

# Core Django URL's 
urlpatterns = [
    path('', serve, {settings.ANGULAR_APP_DIR: 'index.html'}),
    path(r'admin/', admin.site.urls),
]

# App based URL's
urlpatterns += [
    path(r'sabar/', include('coreEngine.urls', namespace="coreEngine")),
]
