from sys import path

from django.conf import urls
from django.contrib import admin

from bad_influence.pages import HomePageView
from django.contrib.auth import views as auth_views

# urlpatterns.append(path(r"^new/$", DemoIndex.as_view(), name='demo'))

"""
def get_urlpatterns():
    urlpatterns = [
        # urls.url(r'^$', RedirectView.as_view(url='/demo', permanent=True)),
        urls.url(r'^login/$', LoginView.as_view(), name='login'),
        urls.url(r'^logout/$', LogoutView.as_view(), name='logout'),
        urls.url(r'^demo/$', DemoIndex.as_view(), name='demo'),

        urls.url(r'^admin/', admin.site.urls),
    ]
"""

urlpatterns = [

    # urls.url(r'^$', RedirectView.as_view(url='/demo', permanent=True)),
    # urls.url(r'^login/$', LoginView.as_view(), name='login_custom'),
    # urls.url(r'^login/$', LogoutView.as_view(), name='logout'),
    urls.url(r'^', HomePageView.as_view(), name='homepage'),
    urls.url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='bad_influence/registration/login.html'), name='homepage'),
    # urls.url(r"^", HomePageView.as_view(), name='homepage'),
    urls.url(r'^admin/', admin.site.urls),
]
