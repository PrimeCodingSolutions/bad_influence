import vanilla
from decorator import append
from django.contrib.auth import admin
from django.shortcuts import render
from django.urls import path
from otree import urls
from otree.channels.consumers import CreateSession
from otree.urls import LoginView, LogoutView, urlpatterns


class HomePageView(vanilla.TemplateView):
    template_name = 'ku_platform/HomePage.html'

    def homepage(self):
        return render(self, 'ku_platform/HomePage.html')


urlpatterns.append(path('homepage/', HomePageView.as_view()))
