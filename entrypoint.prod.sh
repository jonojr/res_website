#!/bin/sh

echo "Waiting for postgres..."

    while ! nc -z db 5432; do
      sleep 0.1
    done

    echo "PostgreSQL started"

python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput

exec "$@"