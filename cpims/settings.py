"""
Django settings for cpims project.

Generated by 'django-admin startproject' using Django 1.8.4.
"""

import os
from datetime import timedelta
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'h34yo5l8c8!edb%^b@3j-i^gc$e)fcjnw_9jm4a^%jbq&*41+@'

FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'


ALLOWED_HOSTS = ['*']

cpims_db_host = os.environ.get(
    'CPIMS_HOST') if os.environ.get('CPIMS_HOST') else '127.0.0.1'
cpims_db_pass = os.environ.get(
    'CPIMS_PASSWORD') if os.environ.get('CPIMS_PASSWORD') else ''
cpims_db_instance = os.environ.get(
    'CPIMS_DB') if os.environ.get('CPIMS_DB') else ''
cpims_db_port = os.environ.get(
    'CPIMS_PORT') if os.environ.get('CPIMS_PORT') else ''
cpims_db_user = os.environ.get(
    'CPIMS_DBUSER') if os.environ.get('CPIMS_DBUSER') else ''
cpims_debug = eval(os.environ.get(
    'CPIMS_DEBUG')) if os.environ.get('CPIMS_DEBUG') else True

DEBUG = cpims_debug

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cpovc_main',
    'cpovc_auth',
    'cpovc_registry',
    'cpovc_forms',
    'cpovc_gis',
    'cpovc_access',
    'cpovc_settings',
    'crispy_forms',
    'crispy_bootstrap3',
    'cpovc_ovc',
    'import_export',
    'rest_framework',
    'data_cleanup',
    'cpovc_offline_mode',
    'cpovc_manage',
    'notifications',
    'cpovc_help',
    'cpovc_preventive',
    'cpovc_pmtct',
    'cpovc_dashboard',
    'cpovc_dreams',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'cpovc_api',
    'cpovc_dashboards',
    'cpovc_mobile',
    'cpovc_hes',
    'django.contrib.humanize',
    'drf_spectacular',
    'drf_spectacular_sidecar',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'cpovc_access.middleware.AuthenticationPolicyMiddleware',
    # 'cpovc_auth.middleware.UserRestrictMiddleware',
    # 'cpovc_access.middleware.FailedLoginMiddleware',

]

ROOT_URLCONF = 'cpims.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cpovc_main.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'cpims.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': cpims_db_instance,
        'USER': cpims_db_user,
        'PASSWORD': cpims_db_pass,
        'HOST': cpims_db_host,
        'PORT': cpims_db_port, },
    'reporting': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': cpims_db_instance,
        'USER': cpims_db_user,
        'PASSWORD': cpims_db_pass,
        'HOST': '41.89.94.104',
        'PORT': cpims_db_port, }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DOCUMENTS_URL = '/documents/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'reports')

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

AUTH_USER_MODEL = 'cpovc_auth.AppUser'

# AUTHENTICATION_BACKENDS = ['cpovc_auth.backends.CPOVCAuthenticationBackend']
# AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOW_NATIONAL_ID_LOGIN = True

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap3"
CRISPY_TEMPLATE_PACK = "bootstrap3"

# to find out what this does
IS_CAPTURE_SITE = False

GIT_ROOT = ''

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

DEFAULT_FROM_EMAIL = 'CPIMS Kenya <%s>' % EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# Session variables
SESSION_COOKIE_AGE = 3 * 60 * 60
SESSION_SAVE_EVERY_REQUEST = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

AXES_LOCKOUT_TEMPLATE = 'locked.html'
AXES_COOLOFF_TIME = 0.25

PASSWORD_CHANGE_POLICIES = (
    ('cpovc_access.password_change.PasswordChangeExpired', {}),
    ('cpovc_access.password_change.PasswordChangeTemporary', {}),
)

PASSWORD_STRENGTH_POLICIES = (
    ('cpovc_access.password_strength.PasswordMinLength', {}),
    ('cpovc_access.password_strength.PasswordContainsUpperCase', {}),
    ('cpovc_access.password_strength.PasswordContainsLowerCase', {}),
    ('cpovc_access.password_strength.PasswordContainsNumbers', {}),
    ('cpovc_access.password_strength.PasswordContainsSymbols', {}),
    ('cpovc_access.password_strength.PasswordUserAttrs', {}),
    ('cpovc_access.password_strength.PasswordLimitReuse', {}),
    ('cpovc_access.password_strength.PasswordDisallowedTerms', {
        'terms': ['cpims']
    }),
)

AUTHENTICATION_POLICIES = (
    ('cpovc_access.authentication.AuthenticationBasicChecks', {}),
    ('cpovc_access.authentication.AuthenticationDisableExpiredUsers', {}),
)

DOCUMENT_ROOT = os.path.join(BASE_DIR, 'templates/documents')

CSRF_FAILURE_VIEW = 'cpims.views.csrf_failure'

OFFLINE_MODE_CAPABILITY_ENABLED = eval(
    os.environ.get('CAN_WORK_OFFLINE', 'False'))

# kmhfl API
KMHFL_USERNAME = '10004'
KMHFL_PASSWORD = 'public'
KMHFL_SCOPE = 'read'
KMHFL_CLIENTID = ''
KMHFL_CLIENT_SECRET = ''
KMHFL_API_BASE_URL = ''
KMHFL_FACILITY_BASE_URL = ''
KMHFL_LOGIN_URL = ''
KMHFL_GRANT_TYPE = ''
KMHFL_SUBCOUNTY_BASE_URL = ''
KMHFL_TOKEN_URL = ''

# NASCOP API
NASCOP_URL = 'https://api.nascop.org/vl/ver2.0/'

NASCOP_API_BASE_URL = os.environ.get(
    'NASCOP_API_BASE_URL') if os.environ.get(
    'NASCOP_API_BASE_URL') else NASCOP_URL + 'patient/results/'
NASCOP_LOGIN_URL = os.environ.get(
    'NASCOP_LOGIN_URL') if os.environ.get(
    'NASCOP_LOGIN_URL') else NASCOP_URL + 'login'
NASCOP_EMAIL = os.environ.get(
    'NASCOP_EMAIL') if os.environ.get(
    'NASCOP_EMAIL') else ''
NASCOP_PASSWORD = os.environ.get(
    'NASCOP_PASSWORD') if os.environ.get(
    'NASCOP_PASSWORD') else ''

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
LOGIN_URL = 'login'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'UPDATE_LAST_LOGIN': True,
}

SPEC_DESC = """Various APIs for child protection workflows. Registration and Management
               of organization Unit (Government and Non Government),
               Persons (Workforce, Children and Caregivers).
               Case Management for DCS (Case Record sheet, Alternative Care,
               Statutory and Charitable Institution care 
               and OVC Case Management (F1A, F1B, Case Plan, CPARA, HIV management, HIV Risk Screening).
               <hr><br><a href='/api/'>API Home (Click here)</a>"""

SPECTACULAR_SETTINGS = {
    "TITLE": "Child Protection Information Management System",
    "DESCRIPTION": SPEC_DESC,
    "VERSION": "1.0.0",
    "PREPROCESSING_HOOKS": [],
    # Custom Spectacular Settings
    "EXCLUDE_PATH": [reverse_lazy("schema")],
}
# "spectacular.hooks.remove_apis_from_list"

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
