from cpsite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j^p*30o)fa6oj%ik_$1=jdo-+ne+mqsvetq2mzaqprc-9j8lq0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['metisbt.ir', 'www.metisbt.ir']

# sites
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'metisbti_meti',
        'USER': 'metisbti_meti',
        'PASSWORD': 'NzLM9B,BgZ)N',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = '/home/metisbti/public_html/static'
MEDIA_ROOT = '/home/metisbti/public_html/media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

#to avoid transmitting the CSRF cookie over HTTP accidentally.
CSRF_COOKIE_SECURE = True

#to avoid transmitting the session cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# SSL
SECURE_SSL_REDIRECT = True


# HTTPS
SECURE_HSTS_SECONDS = 86400  
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True