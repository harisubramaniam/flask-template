import os, sys
import logging
from logging.handlers import RotatingFileHandler

#
# Look for the "Change this" lines. 
# You may need to change /dev/ to /live/ in locations as well
#


# Change this
# os.environ['APP_NAME'] = '/mnt/content.azcentral.com/dev/www.azcentral.com/htdocs/app_name/configs/prod.py'

# Activate your virtual env

#Change this
activate_env=os.path.expanduser("/mnt/content.azcentral.com/dev/www.azcentral.com/htdocs/app_name/fca/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

# Change this
# Add the app's directory to the PYTHONPATH
sys.path.append('/mnt/content.azcentral.com/dev/www.azcentral.com/htdocs/app_name/')
from run import app as application

#Change this
# logging
handler = RotatingFileHandler('/tmp/app_name.log', maxBytes=10000000, backupCount=1)
formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
application.logger.addHandler(handler)
