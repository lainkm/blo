#coding=utf8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tmp/test.db')
	# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:666666@127.0.0.1:5432/blog'
	# SQLALCHEMY_TRACK_MODIFICATIONS = True 为了消除warning，但是这一句加上，在保存到数据库会卡死？？？

	AUTHOR = 'Lainly'
	POSTS_PRE_PAGE = 5

	# this is useful for submitting markdow files
	# when publish new articles
	TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
	SECRET_KEY = 'xixixixihahahhahah'
	TOKEN = os.environ.get('TOKEN')

	@staticmethod
	def init_app(app):
		pass

# config = {
# 	'deflaut': Config
# }
# 	 