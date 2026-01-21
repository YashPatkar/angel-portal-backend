#!/usr/bin/env bash
set -o errexit

uv pip install -r requirements.txt
uv run python manage.py collectstatic --noinput
uv run python manage.py migrate
