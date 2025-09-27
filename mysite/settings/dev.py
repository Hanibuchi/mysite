from .base import *
try:
    from .local_secrets import *
except ImportError:
    print("No local_secrets.py file found")

ALLOWED_HOSTS = ["127.0.0.1"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'