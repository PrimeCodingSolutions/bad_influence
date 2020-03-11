from django.urls import path, include
from bad_influence import pages
from otree.urls import urlpatterns

app_name = "bad_influence"

## Appending URLs to Otree's custom URLs

urlpatterns.append(path('home/', pages.HomePage.as_view()))
urlpatterns.append(path('', include('django.contrib.auth.urls')))

