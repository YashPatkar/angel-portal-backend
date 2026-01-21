#!/usr/bin/env bash
uv run gunicorn backend.wsgi:application
