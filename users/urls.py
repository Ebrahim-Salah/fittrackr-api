from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register),  # This is the route to the register API
]