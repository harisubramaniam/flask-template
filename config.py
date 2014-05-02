import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'xxx'

SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/my_database_name'