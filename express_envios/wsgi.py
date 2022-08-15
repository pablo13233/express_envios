
import os
import sys
path = '/var/www/html/express_envios'
if path not in sys.path:
   sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "express_envios.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
