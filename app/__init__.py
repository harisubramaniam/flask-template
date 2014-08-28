from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate

app = Flask(__name__)
app.config.from_object('configs.default.CommonConfig')
app.config.from_envvar('APP_NAME', silent=True)

# Hacked Flask-SqlAlchemy to support NullPool. You must pip install from cbronazc's fork as documented in install.txt
class MySQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        options['pool_size'] = None
        super(MySQLAlchemy, self).apply_driver_hacks(app, info, options)
db = MySQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)

from app import models, views


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error':'Not found'}), 404

@app.errorhandler(500)
def error(error):
    return jsonify({'error':'Something went wrong'}), 500


# Error emails
# if not app.debug:
#   from common import error_emailer
#   error_mail_handler = error_emailer.setup_error_mail_handler(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
#   app.logger.addHandler(error_mail_handler)
