from django.contrib import admin
from django.urls import path, include

# Core Django URL's 
urlpatterns = [
    path(r'admin/', admin.site.urls),
    # path(r'auth/', obtain_auth_token),
]

# App based URL's
urlpatterns += [
    path(r'', include('coreEngine.urls', namespace="coreEngine")),
    path(r'ai/', include('AIEngine.urls', namespace="AIEngine")),
]
