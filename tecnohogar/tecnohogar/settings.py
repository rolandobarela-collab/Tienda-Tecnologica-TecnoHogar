from pathlib import Path
<<<<<<< HEAD
=======
import os
>>>>>>> origin/rolo

# BASE
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD
SECRET_KEY = 'django-insecure-4$jhop^&1@abi=c)x36_u*=jsnz$*)5cvzj+k@!3_+j!(-d#*z'
<<<<<<< HEAD

DEBUG = False

ALLOWED_HOSTS = ['.onrender.com']

=======
DEBUG = False
ALLOWED_HOSTS = ['*']
>>>>>>> origin/rolo

# APLICACIONES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD

    'usuarios',
]


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

=======
    'django.contrib.humanize',
    'usuarios',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
>>>>>>> origin/rolo
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

<<<<<<< HEAD

ROOT_URLCONF = 'tecnohogar.urls'


# TEMPLATES
=======
ROOT_URLCONF = 'tecnohogar.urls'

>>>>>>> origin/rolo
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.parent / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

<<<<<<< HEAD

WSGI_APPLICATION = 'tecnohogar.wsgi.application'


# BASE DE DATOS
=======
WSGI_APPLICATION = 'tecnohogar.wsgi.application'

>>>>>>> origin/rolo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

<<<<<<< HEAD

# VALIDACIONES
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


# IDIOMA Y ZONA
LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# ARCHIVOS ESTÁTICOS
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR.parent / "static",
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# LOGIN
LOGIN_URL = 'login'


# DEFAULT
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORREO
=======
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.parent / "static",
]
STATIC_ROOT = BASE_DIR.parent / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media')

LOGIN_URL = 'login'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

>>>>>>> origin/rolo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
<<<<<<< HEAD
EMAIL_HOST_USER = 'roliruana@gmail.com'
EMAIL_HOST_PASSWORD = 'ehwi yaqc evym ijuf'
DEFAULT_FROM_EMAIL = 'roliruana@gmail.com'
=======
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
>>>>>>> origin/rolo
