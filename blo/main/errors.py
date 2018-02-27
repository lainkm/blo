from flask import render_template, request
from . import main


@main.app_errorhandler(404)
def page_not_found(error):
  """
  error是<class 'werkzeug.exceptions.NotFound'>对象，python3中使用str代替unicode
  """
  # title = repr(error)  # 或str(error)
  # message = error.description
  # message = str(error)
  title = str(error)
  return render_template('errors.html',
                         title=title)


@main.app_errorhandler(500)
def internal_server_error(error):
  # title = repr(error)
  # message = error.description
  # message = str(error)
  title = str(error)
  return render_template('errors.html',
                         title=title)
