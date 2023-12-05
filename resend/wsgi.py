"""
WSGI config for resend project.
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resend.settings")

if os.getenv("STATIC_ENABLED", "1") == "1":
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = get_wsgi_application()
