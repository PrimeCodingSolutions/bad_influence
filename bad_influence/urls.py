from otree.urls import urlpatterns
from django.urls import path
from bad_influence import pages


app_name = "bad_influence"


urlpatterns.append(path('home/', pages.HomePage.as_view()))


