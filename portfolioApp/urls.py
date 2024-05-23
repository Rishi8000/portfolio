from django.contrib import admin
from django.urls import path
from portfolioApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/',views.skills, name='skills'),
    path('aboutMe/',views.aboutMe, name='aboutMe'),
    path('contact/',views.contact, name='contact'),
]
