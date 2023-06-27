#!/usr/bin/env bash
# start-server.sh

echo "Hello from Project HAPA"

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (echo "creating superuser ${DJANGO_SUPERUSER_USERNAME}" && python djangobaseproject/manage.py createsuperuser --no-input --noinput --email 'blank@email.com' )
fi
python manage.py collectstatic --no-input 
python manage.py migrate --no-input
gunicorn djangobaseproject.wsgi --bind 0.0.0.0:8010 --workers 3 --timeout 600 & nginx -g "daemon off;"
