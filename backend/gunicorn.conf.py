# file gunicorn.conf.py
# coding=utf-8

import multiprocessing
import os

loglevel = 'info'
# errorlog = os.path.join(_VAR, 'log/api-error.log')
# accesslog = os.path.join(_VAR, 'log/api-access.log')
errorlog = "-"
accesslog = "-"
# bind = 'unix:%s' % os.path.join(_VAR, 'run/gunicorn.sock')
APP_PORT = os.environ.get('APP_PORT', 5000)
bind = f'0.0.0.0:{APP_PORT}'
# workers = 3
workers = 1  # multiprocessing.cpu_count() * 2 + 1
timeout = 3 * 60
# 3 minutes
keepalive = 24 * 60 * 60  # 1 day
capture_output = True
