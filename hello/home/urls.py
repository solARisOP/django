from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name ='home'), # if the request is blank then call index function in views
    path("about", views.about, name ='about'), # if the request is about then call about function in views
    path("services", views.services, name ='services'), # if the request is services then call services function in views
    path("contact", views.contact, name ='contact'), # if the request is contact then call contact function in views
]