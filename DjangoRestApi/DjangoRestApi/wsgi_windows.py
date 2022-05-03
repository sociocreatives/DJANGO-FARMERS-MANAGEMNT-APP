activate_this = 'C:/wamp64/www/kiloapi/DjangoRestApi/env/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
# exec(open(activate_this).read(),dict(__file__=activate_this))
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/wamp64/www/kiloapi/DjangoRestApi/env/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/wamp64/www/kiloapi')
sys.path.append('C:/wamp64/www/kiloapi/DjangoRestApi')

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoRestApi.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoRestApi.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()