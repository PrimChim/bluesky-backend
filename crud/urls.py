from django.contrib import admin
from django.urls import path, include
from frontend.urls import urlpatterns as frontend_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(frontend_urls)),
]
