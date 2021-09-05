"""
WSGI config for A_show_me_da_post project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A_show_me_da_post.settings')

if settings.DEBUG:
    application = get_wsgi_application()
else:
    application = Cling(MediaCling(get_wsgi_application()))
