import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Get db credentials, add "db.text" in the configs folder with just your string
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
db_file = open(os.path.join(__location__, 'db.txt'));
db_creds = db_file.read().rstrip('\n')
db_file.close()

class CommonConfig(object):
    SECRET_KEY = 'abc987'
    SQLALCHEMY_DATABASE_URI = db_creds
    DEBUG = True
    CACHE_TIME = 60 # 1 minute

    # Uncomment for mail
    #
    # Email server
    # MAIL_DEBUG = False
    # MAIL_SERVER = 'newman.azcentral.com'
    # MAIL_PORT = 25
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = False
    # MAIL_USERNAME = ''
    # MAIL_PASSWORD = ''

