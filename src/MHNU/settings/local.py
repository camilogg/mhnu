from .base import *
import socket

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS += ['debug_toolbar', 'django_extensions']

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG
}

WEASYPRINT_BASEURL = 'localhost'

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
