from core.settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k(is7f%*f=qen9ji#jx-vc*6g!&#c7t*xqbcxt&fml&x5+o44u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT=BASE_DIR/'statics'
MEDIA_ROOT=BASE_DIR/'medias'


SITE_ID=2
ROBOTS_USE_HOST = False