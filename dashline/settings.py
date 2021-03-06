# Django settings for dashline project.

import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_DIR, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_DIR, 'external_apps'))

ADMINS = (
    ('diofeher', 'diofeher@gmail.com'),
    ('chronos', 'philipe.rp@gmail.com'),
    ('ikke', 'ikkibr@gmail.com'),
)

_ = lambda s: s
LANGUAGES = (
    ('en', _('English')),
    ('pt-br', _('Portuguese (Brazil)')),
)

MANAGERS = ADMINS

DATABASES = {
    # DEFAULT, to overwrite, write your own at settings_local.py
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'banco.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media.dashline.chronosbox.org/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h!4eu(6)+pvaymw&rd4ut)nclsr-uc6eqxl8ie+ogu@gqynbyq'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'dashline.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    #locals
    'users',
    'timeline',
    #external
    'registration',
    'profiles',
    'pagination',
    'haystack',
)

ACCOUNT_ACTIVATION_DAYS = 7

AUTH_PROFILE_MODULE = 'users.UserProfile'

LOGIN_REDIRECT_URL = '/profiles/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Search stuff
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'dashline.search_sites'

HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_DIR, 'dashline_index')

#Settings local
try:
    execfile(os.path.join(PROJECT_DIR, 'settings_local.py'), globals(), locals())
except IOError:
    pass
