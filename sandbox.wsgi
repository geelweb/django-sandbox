import os, sys
sys.path.append('/home/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'sandbox.settings'
os.environ['APPLICATION_ENV'] = 'production'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

