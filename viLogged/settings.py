# Django settings for viLogged project.
import os
import sys
import platform
SYS_OS = platform.system()

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PARENT = os.path.dirname(PROJECT_ROOT)
sys.path.insert(0, PROJECT_ROOT)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
if SYS_OS is 'Windows':
    DATABASES = {
        'default': {
            'NAME': 'viLogged',
            'ENGINE': 'sqlserver_ado',
            'HOST': 'musa\\SQLEXPRESS',
            'USER': '',
            'PASSWORD': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite'),
            'ENGINE': 'django.db.backends.sqlite3',
            'HOST': 'localhost',
            'USER': '',
            'PASSWORD': '',
        }
    }
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Lagos'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%2=)0ug0*=wyr5v6v=%_trw!sjy60x98*$#%%0o26ut%m!5h0)'

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
    'corsheaders.middleware.CorsMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'viLogged.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'viLogged.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'djoser',
    'django_extensions',
    'core',
    'appointments',
    'staff',
    'grappelli',
    'django.contrib.admin',
    'django_twilio',
    'corsheaders',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

TWILIO_ACCOUNT_SID = 'AC9bea919627d63c232851c8e56faf6435'
TWILIO_AUTH_TOKEN = '0f37345fc2c507b4f4ae31c82fdee6ab'
TWILIO_DEFAULT_CALLERID = 'viLogged VMS'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'iphaselimited@gmail.com'
EMAIL_HOST_PASSWORD = '*ip4life#'
DEFAULT_FROM_EMAIL = 'iphaselimited@gmail.com'


FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, "core/fixtures"),
)

FILE_UPLOAD_PERMISSIONS = 0644
LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/"

REST_FRAMEWORK = {
# Use hyperlinked styles by default.
# Only used if the `serializer_class` attribute is not set on a view.
'DEFAULT_MODEL_SERIALIZER_CLASS':
'rest_framework.serializers.HyperlinkedModelSerializer',
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
),
# # Use Django's standard `django.contrib.auth` permissions,
# # or allow read-only access for unauthenticated users.
# 'DEFAULT_PERMISSION_CLASSES': [
# 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
# ]
# Allow anything
'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
# http://www.django-rest-framework.org/api-guide/filtering
'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
}

DJOSER = {
    'DOMAIN': 'vilogged',
    'SITE_NAME': 'vilogged',
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',

}



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:9000',
    'localhost:8000',
    'localhost/',
)
