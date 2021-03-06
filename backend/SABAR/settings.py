import os
from . import environments


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f13cgz^ha9j1pde^gk45q3tm+4cv&=%r#%$_i%fdu9i^x05czb'
ADMIN_USER_NAME = environments.get_value('ADMIN_USER_NAME')
ADMIN_PASSWORD = environments.get_value('ADMIN_PASSWORD')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environments.get_value('DEBUG')
DOMAIN = environments.get_value('DOMAIN')
ALLOWED_HOSTS = environments.get_value('ALLOWED_HOSTS')

CORS_ORIGIN_ALLOW_ALL = True


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    # 'rest_framework.authtoken',
    # 'corsheaders',
    'taggit',
    'django_extensions',

    'coreEngine',
    'utility',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    
    # To Help Serve Angular
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'spa.middleware.SPAMiddleware',
]

ROOT_URLCONF = 'SABAR.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'SABAR.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = environments.get_value('DATABASES')


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    # 'DEFAULT_PERMISSIONS_CLASSES' : [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.TokenAuthentication',
    # ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'authentication.csrf_exempt_session_authentication.CsrfExemptSessionAuthentication',
    # ),
    # 'EXCEPTION_HANDLER': 'utility.exceptionHandlers.custom_exception_handler.custom_exception_handler',
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ANGULAR_APP_DIR = environments.get_value('ANGULAR_APP_DIR')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = environments.get_value('STATIC_URL')
STATIC_ROOT = environments.get_value('STATIC_ROOT')
STATICFILES_STORAGE = 'spa.storage.SPAStaticFilesStorage'
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(ANGULAR_APP_DIR)   # Required for angular app dist serving
]

# Django-Taggit
TAGGIT_CASE_INSENSITIVE = True

from utility.logging.logging import LogProject
LogProject.init_logger()
