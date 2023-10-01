from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("therapiest-contact.html/", views.contact, name="contact"),
]

