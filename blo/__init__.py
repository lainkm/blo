#coding=utf8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config

# app = Flask(__name__)
# POSTS_PRE_PAGE = 3

# app.config.from_object('config')
# from . import utils
# from . import views

db = SQLAlchemy()
bootstrap=Bootstrap()


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	Config.init_app(app)
	db.init_app(app)
	bootstrap.init_app(app)
	print(app)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	print(app)

	def format_date(dateobj):
		return dateobj.strftime(
	'%b %d,%Y')


	def format_date_weekday(dateobj):
		return dateobj.strftime(
	'%A %b %d,%Y')


	def format_datetime(dateobj):
		return dateobj.strftime(
	'%A %b %d,%Y %H:%M:%S')

	app.jinja_env.globals['format_date'] = format_date
	app.jinja_env.globals['format_date_weekday'] = format_date_weekday
	app.jinja_env.globals['format_datetime'] = format_datetime

	return app