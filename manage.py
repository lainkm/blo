#!/usr/bin/env python
#coding=utf8

from blo import create_app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def say_hi():
	print('hello')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    manager.run()
