#!/usr/bin/env bash
set -o errexit

# Install dependencies using uv
uv pip install -r requirements.txt

# Run Django commands through uv
uv run python manage.py collectstatic --noinput
uv run python manage.py migrate
