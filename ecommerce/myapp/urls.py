from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('home/',views.home)
]