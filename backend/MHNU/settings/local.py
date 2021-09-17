from .base import *

DEBUG = True

INSTALLED_APPS += ['debug_toolbar', 'django_extensions']

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG
}

HOST_URL = os.environ.get('HOST_URL')
HOST_URL_FRONTEND = os.environ.get('HOST_URL_FRONTEND')
