from django.urls import path
from .views import register, login

urlpatterns = [
    path('register/', register),  # This is the route to the register API
    path('login/', login),
]