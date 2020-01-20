import os

from werkzeug.middleware.proxy_fix import ProxyFix

from src.app import app

if os.environ.get('REMOTE_DEBUG', False):
    import pydevd_pycharm
    pydevd_pycharm.settrace('localhost', port=5100, stdoutToServer=True, stderrToServer=True)

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
