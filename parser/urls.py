from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vacations/", views.vacations, name="vacations"),          
]