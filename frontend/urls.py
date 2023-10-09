from django.urls import path
from .views import index, about, contact, reservation

app_name = 'frontend'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('reservation/', reservation, name='reservation'),
]
