#!flask/bin/python
from app import app, manager
from flask.ext.migrate import Migrate, MigrateCommand

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
