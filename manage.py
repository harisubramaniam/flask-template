#!flask/bin/python
from app import manager
from flask.ext.migrate import MigrateCommand

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
