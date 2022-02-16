#!/bin/sh

wait-for-it db:5432

case $1 in
  python | gunicorn)
    python manage.py migrate
    python manage.py collectstatic --no-input
  ;;
  watchmedo | celery)
    wait-for-it backend:8000
esac

exec "$@"