"""Vercel serverless entry point for the Django application."""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zanzora.settings")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
