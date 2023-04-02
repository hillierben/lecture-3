from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("ben", views.ben, name="ben"),
    path("becky", views.becky, name="becky"),
]