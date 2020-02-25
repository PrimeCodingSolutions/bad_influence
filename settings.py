import os
from os import environ
import dj_database_url

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
LANGUAGE_CODE = 'en'

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
INSTALLED_APPS = ['otree']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}
