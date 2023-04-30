from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("numpy.html", views.numpy, name="numpy"),
]
