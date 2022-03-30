from unicodedata import name
from django.urls import path

from equipment.views import home, ping, floor_level, floor


urlpatterns = [
    path('', home, name='home'),
    path('ping/<int:id>', ping, name='ping'),
    path('floor_level/<int:id>', floor_level, name='floor_level'),
    path('floor/', floor, name='floor'),

]