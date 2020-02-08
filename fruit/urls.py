from django.urls import path
from .views import home,fruitt
urlpatterns = [
    path('fruitt/',fruitt,name='fruitt'),
    path('',home,name='home'),
]