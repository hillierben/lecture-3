from django.urls import path
from django.http import HttpRequest

from . import views

app_name = "newyear"

urlpatterns = [
    path("", views.index, name="index"),
]