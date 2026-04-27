from pathlib import Path

# BASE
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD
SECRET_KEY = 'django-insecure-4$jhop^&1@abi=c)x36_u*=jsnz$*)5cvzj+k@!3_+j!(-d#*z'
DEBUG = True
ALLOWED_HOSTS = []

# APLICACIONES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'usuarios',  # MI APP
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tecnohogar.urls'

# TEMPLATES (CONECTA TU FRONTEND)
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

WSGI_APPLICATION = 'tecnohogar.wsgi.application'

# BASE DE DATOS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

# ARCHIVOS ESTÁTICOS (CSS, JS, IMÁGENES)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR.parent / "static",
]

# LOGIN (para más adelante)
LOGIN_URL = 'login'

# DEFAULT
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CONFIGURACIÓN DE CORREO
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'roliruana@gmail.com'  # correo Gmail
EMAIL_HOST_PASSWORD = 'Rolandobarelanumero5'  # contraseña de app
DEFAULT_FROM_EMAIL = 'roliruana@gmail.com'
