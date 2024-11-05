from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', create_profile, name='create_profile'),
]