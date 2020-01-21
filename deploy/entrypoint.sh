#!/usr/bin/env bash

flask db upgrade
gunicorn -c gunicorn.conf.py wsgi:app