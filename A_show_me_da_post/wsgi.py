"""
WSGI config for A_show_me_da_post project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling
from django.conf.global_settings import DEBUG

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A_show_me_da_post.settings')

development_app = Cling(MediaCling(get_wsgi_application()))
production_app = get_wsgi_application()

application = development_app if DEBUG else production_app
