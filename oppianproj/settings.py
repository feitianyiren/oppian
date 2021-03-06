# Django settings for oppian project.

import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = True

ADMINS = (
    ('Web Admins Oppian', 'web-admins@oppian.com'),
)

MANAGERS = ADMINS

CONTACT_RECIPIENTS = (
    ('Contact Oppian', 'contact@oppian.com'),
)

# only serve media in Django in debug mode as in release mode, it is served by Apache
SERVE_MEDIA = DEBUG

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_ROOT, '.sqlite.db')              # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-GB'

SITE_ID = 1
SITE_NAME = 'Oppian'
# work out the domain name
# for local debugging on ports other than 80, this should be overridden in settings_local.py 
import socket
SITE_DOMAIN = socket.gethostname()


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT_LOCAL = os.path.join(PROJECT_ROOT, 'media/')
MEDIA_ROOT = ''

# if SHORTENER_REQUIRES_LOGIN is True, then only logged in users can submit new URLs
SHORTENER_REQUIRES_LOGIN = True

# add the template context processor for the latest tweet
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    "oppianapp.context_processors.settings",
    'django.core.context_processors.request',
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/m/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

# Make this unique, and don't share it with anybody.
# SECRET_KEY = '' # provided by puppet 

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "templates").replace('\\', '/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.humanize',

    # basic apps http://github.com/nathanborror/django-basic-apps/tree/master
    'basic.*',

    # url shortener git://github.com/nileshk/url-shortener.git 
    'url_shortener',

    # web-crawler robot control hg clone http://bitbucket.org/jezdez/django-robots/ 
    'robots',

    # tagging http://code.google.com/p/django-tagging/
    'tagging',

    'contact_form',

    # django command extensions http://github.com/django-extensions
    'django_extensions',

    # google analytics - from http://github.com/montylounge/django-google-analytics
    'google_analytics',

    # http://code.google.com/p/django-filebrowser/wiki/filebrowser_3
    'filebrowser',
    
    # http://django-tinymce.googlecode.com/svn/trunk/docs/.build/html/index.html
    'tinymce',

    # oppian web-site specific code including static pages
    'oppianapp',
    
    # south dbmigration
    'south',
)

# build
AWS_BUILD_BUCKET_NAME = 'oppian-website-releases'
BUILD_VERSION = ('0', '2')
BUILD_APPNAME = 'oppian'
BUILD_IGNORE = (
    os.path.normpath(os.path.join(PROJECT_ROOT, 'ec2')),
    os.path.normpath(os.path.join(PROJECT_ROOT, 'rightscripts')),
    os.path.normpath(os.path.join(PROJECT_ROOT, 'support_files')),
)

# email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'www@oppian.com'
EMAIL_HOST_PASSWORD = '4E6993'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# default from address for errors
import socket
SERVER_EMAIL = '"%s" <www@oppian.com>' % socket.gethostname()
# default from address for normal email
DEFAULT_FROM_EMAIL = 'www@oppian.com'

# fixture
FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, "fixtures"),
)

# Google Analytics
GOOGLE_ANALYTICS_MODEL = True

# filebrowser
FILEBROWSER_URL_FILEBROWSER_MEDIA = '%sfilebrowser/' % MEDIA_URL
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_SAVE_FULL_URL = False       # if true, FileBrowserField errors because of s3 url
FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 104, 'height': 104, 'opts': 'upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (140px)', 'width': 140, 'height': '', 'opts': ''},
    'small': {'verbose_name': 'Small (300px)', 'width': 300, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (460px)', 'width': 460, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (620px)', 'width': 620, 'height': '', 'opts': ''},
    'cropped': {'verbose_name': 'Cropped (60x60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'croppedthumbnail': {'verbose_name': 'Cropped Thumbnail (140x140px)', 'width': 140, 'height': 140, 'opts': 'crop'},
    'blog': {'verbose_name': 'Blog Thumbnail (210x143)', 'width': 196, 'height': 110, 'opts': 'upscale crop'},
}

# TODO: move s3 default storage into prod and dev settings
# django storages: http://code.welldev.org/django-storages/wiki/S3Storage
DEFAULT_FILE_STORAGE = 'backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'oppian-dev-files'
from S3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
AWS_QUERYSTRING_AUTH = False

# tinymce: http://django-tinymce.googlecode.com/svn/trunk/docs/.build/html/installation.html
TINYMCE_JS_URL = '%stinymce/tiny_mce_src.js' % MEDIA_URL
TINYMCE_JS_ROOT = '%s/tinymce' % MEDIA_ROOT_LOCAL
TINYMCE_FILEBROWSER = True
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced", 
    'plugins' : 'syntaxhl', 
    'relative_urls': False,
    'skin' : "o2k7",
    'height': "480",
    'theme_advanced_resizing' : True,
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_buttons3_add' : 'syntaxhl',
    'extended_valid_elements' : "textarea[cols|rows|disabled|name|readonly|class]" 
}

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from settings_local import *
except ImportError:
    pass
