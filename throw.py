from sys import path

from django.conf import urls
from django.contrib import admin
from otree.urls import get_urlpatterns
from bad_influence.pages import LoginView, DemoIndex
from django.contrib.auth import views as auth_views

# urlpatterns.append(path(r"^new/$", DemoIndex.as_view(), name='demo'))

"""

import os
from os import environ
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SENTRY_DSN = 'http://2d6137799b914e1693146c5011f39030:46838e8caa374937a91b14b59ebbe164@sentry.otree.org/36'

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'bad_influence',
        'display_name': "bad influence",
        'num_demo_participants': 5,
        'app_sequence': ['bad_influence'],
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'da'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_CUSTOM_NAME = ''

ROOMS = [
    dict(
        name='BadInfluence',
        display_name='Bad Influence - test class'
    )
]

CHANNEL_ROUTING = 'routing.channel_routing'

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = 'g+h6se573b6wbmxl7v0ejjq1cawe(bvk6+rcga0j4g3=^w%5fu'

# if an app is included in SESSION_CONFIGS, you don't need to list it here

INSTALLED_APPS = [
    'bad_influence',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'otree',


]

ROOT_URLCONF = 'otree.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'bad_influence/bad_influence/templates'), os.path.join(BASE_DIR, 'bad_influence/bad_influence/templates', 'bad_influence')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]





DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}


#LOGIN_REDIRECT_URL = '/'

#LOGIN_URL = '/login/'















urlpatterns = [
    # urls.url(r'^$', RedirectView.as_view(url='/demo', permanent=True)),
    urls.url(r'^login/$', LoginView.as_view(), name='login'),
    # urls.url(r'^logout/$', LogoutView.as_view(), name='logout'),
    urls.url(r'^homepage/$', DemoIndex.as_view(), name='demo'),
    urls.url(r'^admin/', admin.site.urls),
]


urlpatterns = [

    # urls.url(r'^$', RedirectView.as_view(url='/demo', permanent=True)),
    # urls.url(r'^login/$', LoginView.as_view(), name='login_custom'),
    # urls.url(r'^login/$', LogoutView.as_view(), name='logout'),
    urls.url(r'^', HomePageView.as_view(), name='homepage'),
    urls.url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='bad_inf luence/registration/bad_influence/templates/bad_influence/login.html'), name='homepage'),
    # urls.url(r"^", HomePageView.as_view(), name='homepage'),
    urls.url(r'^admin/', admin.site.urls),
]
"""
