"""
Django settings for policykit project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Read .env file which contains settings and secrets
env = environ.Env(
    # set default values for environment variables
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    SERVER_URL=(str, "http://127.0.0.1:8000"),
    LOG_FILE=(str, "debug.log"),

    # DEV SECRET! override by setting DJANGO_SECRET_KEY in .env file
    DJANGO_SECRET_KEY=(str, 'kg=&9zrc5@rern2=&+6yvh8ip0u7$f=k_zax**bwsur_z7qy+-')
)
environ.Env.read_env()

DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
SERVER_URL = env("SERVER_URL")
SECRET_KEY = env("DJANGO_SECRET_KEY")
LOGIN_URL = "/login"

# Application definition
INTEGRATIONS = [
    'integrations.slack',
    'integrations.reddit',
    'integrations.discord',
    'integrations.discourse',
    'integrations.github',
    'integrations.opencollective',
    'integrations.loomio',
    'integrations.sourcecred',
    'integrations.sendgrid',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'django_filters',
    'django_tables2',
    'django_extensions',
    'django_db_logger',
    'actstream',
    'metagov.plugins.slack',
    'metagov.plugins.opencollective',
    'metagov.plugins.github',
    'metagov.plugins.sourcecred',
    'metagov.plugins.loomio',
    'metagov.plugins.discord',
    'metagov.plugins.discourse',
    'metagov.plugins.example', #for testing
    'metagov.core',
    'policyengine',
    'constitution'
] + INTEGRATIONS

SITE_ID = 1

import sys
TESTING = sys.argv[1:2] == ["test"]

METAGOV_SETTINGS = {
    "SLACK": {
        "CLIENT_ID": env("SLACK_CLIENT_ID", default=None),
        "CLIENT_SECRET": env("SLACK_CLIENT_SECRET", default=None),
        "SIGNING_SECRET": env("SLACK_SIGNING_SECRET", default=None),
        "APP_ID": env("SLACK_APP_ID", default=None),
    },
    "GITHUB": {
        "APP_NAME": env("GITHUB_APP_NAME", default=None),
        "APP_ID": env("GITHUB_APP_ID", default=None),
        "PRIVATE_KEY_PATH": env("GITHUB_PRIVATE_KEY_PATH", default=None),
    },
    "DISCORD": {
        "CLIENT_ID": env("DISCORD_CLIENT_ID", default=None),
        "CLIENT_SECRET": env("DISCORD_CLIENT_SECRET", default=None),
        "BOT_TOKEN": env("DISCORD_BOT_TOKEN", default=None),
        "PUBLIC_KEY": env("DISCORD_PUBLIC_KEY", default=None),
        "PERMISSIONS": env("DISCORD_PERMISSIONS", default=397821540358),
    },
    "OPENCOLLECTIVE": {
        "USE_STAGING": env("OPENCOLLECTIVE_USE_STAGING", default=False)
    },
    "SENDGRID": {
        "API_KEY": env("SENDGRID_API_KEY", default=None)
    }
}

REDDIT_CLIENT_ID = env("REDDIT_CLIENT_ID", default=None)
REDDIT_CLIENT_SECRET = env("REDDIT_CLIENT_SECRET", default=None)

ACTSTREAM_SETTINGS = {
    'MANAGER': 'policyengine.managers.myActionManager',
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': True,
    'GFK_FETCH_DEPTH': 1,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'policykit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'policykit.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if os.getenv("DOCKER_ENV_CHECK"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = ['integrations.discourse.auth_backends.DiscourseBackend',
                           'integrations.discord.auth_backends.DiscordBackend',
                           'integrations.reddit.auth_backends.RedditBackend',
                           'integrations.slack.auth_backends.SlackBackend',
                           'django.contrib.auth.backends.ModelBackend']


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

PROJECT_NAME = "PolicyKit"


### Logging
import sys
import os

# Set default log level
DEFAULT_LOG_LEVEL_FOR_TESTS = "DEBUG"
DEFAULT_LOG_LEVEL = "DEBUG"

TESTING = sys.argv[1:2] == ["test"]
LOG_LEVEL = DEFAULT_LOG_LEVEL_FOR_TESTS if TESTING else DEFAULT_LOG_LEVEL

# Generate loggers for engine and integrations
loggers = {}
for app in ['policyengine'] + INTEGRATIONS:
    loggers.update({app: {"handlers": ["console", "file"], "level": LOG_LEVEL, "propagate": False}})
# Database logger for policy evaluation logs
loggers["db"] = {"handlers": ["db_log"], "level": DEFAULT_LOG_LEVEL, "propagate": False}
# Set log level to WARN for everything else (imported dependencies)
loggers[""] = {"handlers": ["console", "file"], "level": "WARN"}

# Override for specific apps
loggers['metagov'] = {'handlers': ['console', 'file'], 'level': "DEBUG", "propagate": False}

# Maximum number of log records to keep
DB_MAX_LOGS_TO_KEEP = 5000

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        "console": {"format": "%(name)-12s %(levelname)-8s %(message)s"},
        "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
    },
    'handlers': {
        "db_log": {
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler'
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": env("LOG_FILE"),
            "formatter": "file",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
    },
    'loggers': loggers
}


CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

CELERY_BEAT_FREQUENCY = 60.0

CELERY_BEAT_SCHEDULE = {
    # Evaluate pending policy evaluations every minute
    "evaluate-pending-proposals-beat": {
        "task": "policyengine.tasks.evaluate_pending_proposals",
        "schedule": CELERY_BEAT_FREQUENCY,
    },
    # Poll reddit for updates
    "reddit-listener-beat": {
        "task": "integrations.reddit.tasks.reddit_listener_actions",
        "schedule": CELERY_BEAT_FREQUENCY,
    },
    # Poll discourse for updates
    "discourse-listener-beat": {
        "task": "integrations.discourse.tasks.discourse_listener_actions",
        "schedule": CELERY_BEAT_FREQUENCY,
    },
    # Metagov task for polling external platforms
    "metagov-plugins-beat": {
        "task": "metagov.core.tasks.execute_plugin_tasks",
        "schedule": CELERY_BEAT_FREQUENCY,
    },
}
