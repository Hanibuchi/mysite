from .base import *
try:
    from .local_secrets import *
except ImportError:
    print("No local_secrets.py file found")


ALLOWED_HOSTS = ["hani-tech.com", "www.hani-tech.com"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
        'USER': DEV_DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net' 
EMAIL_HOST_USER = MY_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = MY_EMAIL_HOST_PASSWORD
EMAIL_PORT = MY_EMAIL_PORT
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'hanitech8686@gmail.com' 