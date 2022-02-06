from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(",")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

HOST_URL = os.environ.get("HOST_URL")
HOST_URL_FRONTEND = os.environ.get("HOST_URL_FRONTEND")
