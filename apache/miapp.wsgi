import os
import sys
sys.path = ['/var/www/html/miapp'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'miapp.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
