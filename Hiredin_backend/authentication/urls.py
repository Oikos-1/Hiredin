from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='SignUp'),
    path('login/', views.login, name='SignIn'),
    path('test/', views.example_view, name="test")
]
