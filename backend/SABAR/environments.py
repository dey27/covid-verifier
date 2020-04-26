import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACTIVE_ENVIRONMENT = os.environ.get('environment', 'DEV')

DEV = {
    'STATIC_ROOT': os.path.join(BASE_DIR, 'staticfiles'),
    'STATIC_URL': '/static/',
    'ANGULAR_APP_DIR': os.environ.get('angular_app_dir', os.path.join(BASE_DIR, '../frontend/dist')),
    'DOMAIN': os.environ.get('domain', '127.0.0.1'),
    'DEBUG': os.environ.get('debug', True),
    'ALLOWED_HOSTS': ['localhost', '127.0.0.1', os.environ.get('allowed_hosts')],
    'DATABASES': { # TODO - Should be migrated to postgres in future.
        'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
}

PRODUCTION = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('db_name', 'sabar'),
            'USER': os.environ.get('db_username', 'postgres'),
            'PASSWORD': os.environ.get('db_password', 'postgres'),
            'HOST': os.environ.get('db_host', 'localhost'),
            'PORT': os.environ.get('db_port', '5432'),
        }
    },
}


def get_value(key):
    """
    :param key: for example - DATABASES
    :return: value retrieved based on ACTIVE_ENVIRONMENT
    """
    try:
        return eval('{}.get("{}")'.format(ACTIVE_ENVIRONMENT, key))
    except Exception as e:
        return ""
