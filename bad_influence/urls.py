from django.urls import path, include
from bad_influence import pages
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = "bad_influence"

urlpatterns = [

    path('home/', pages.HomePage.as_view()),


]


