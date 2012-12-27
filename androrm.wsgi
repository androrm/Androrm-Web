import os
import sys

if not '/var/www' in sys.path:
    sys.path.append('/var/www')

os.environ['DJANGO_SETTINGS_MODULE'] = 'androrm.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
