#!/usr/bin/env bash
set -o errexit

pip install --retries 5 --timeout 60 -r requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate