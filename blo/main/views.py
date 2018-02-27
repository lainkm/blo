#coding=utf8

from datetime import datetime
import json
from flask import render_template, request, abort, current_app
from sqlalchemy import and_
from . import main
from .. import db
from ..models import Article, Tag, create_article, delete_article
from ..utils import markdown2html, load_content
from .forms import SearchForm



# @app.route('/')
# @app.route('/<int:page>')
# def index(page=1):
#   """
#   用sqalchemy封装的pagination实现分页
#   """
#   pagination = Article.query.order_by(Article.id.desc()).paginate(page, POSTS_PRE_PAGE, False)
#   return render_template('index.html',
#                          pagination=pagination)

@main.route('/', methods=['GET', 'POST'])
def index():
  """
  用sqalchemy封装的pagination实现分页, 这个直接用url的page。。其实一样
  """
  form = SearchForm()
  if request.method == 'POST':
    search = form.content.data
    print(search)
    page = request.args.get('page', 1, type=int)
    article = Article.query.filter(Article.content.like("%"+search+"%")
                                )
    print(article.all())
    pagination = article.paginate(page, current_app.config['POSTS_PRE_PAGE'], False)
    tags = Tag.query.all()
    return render_template('index.html',
                        tags=tags,
                        form=form,
                         pagination=pagination)
   

  print('haha')
  page = request.args.get('page', 1, type=int)
  pagination = Article.query.order_by(Article.id.desc()).paginate(page, current_app.config['POSTS_PRE_PAGE'], False)
  tags = Tag.query.all()
  return render_template('index.html',
                        tags=tags,
                        form=form,
                         pagination=pagination)


@main.route('/article/<id>')
def show_article(id):
  article = Article.query.get(id)
  article.add_read()
  return render_template('page.html',
                         title=article.title,
                         content=article.content,
                         pub_time=article.pub_time,
                         read_times=article.read_times,
                         tags=article.tags)

@main.route('/tags')
def show_tags():
  tags = Tag.query.all()
  return render_template('tags.html',
                         tags=tags)

@main.route('/tag/<id>')
def show_tag(id):
  tag = Tag.query.get_or_404(id)
  articles = tag.articles.all()
  return render_template('tag.html',
                         tag=tag,
                         entries=articles)

@main.route('/about')
def about():
  content = load_content('about')
  return render_template('page.html',
                         title='About',
                         content=content)


@main.route('/links')
def links():
  content = load_content('links')
  return render_template('page.html',
                         title='Links',
                         content=content)
@main.route('/mark')
def mark():
  content = load_content('mark')
  return render_template('page.html',
                          title='Mark',
                          content=content)

@main.route('/delete', methods=['GET', 'POST'])
def delete():
  if request.method == 'GET':
    abort(404)

  token = request.form.get('token', '')
  if token != current_app.config['TOKEN']:
    return 'invalid access token', 500

  title = request.form.get('title', None)
  if not title:
      return 'no title found', 500

  print(delete_article(title))
  return '', 200


@main.route('/publish', methods=['GET', 'POST'])
def publish():
  if request.method == 'GET':
      abort(404)

  # authorization
  token = request.form.get('token', '')
  if token != current_app.config['TOKEN']:
      return 'invalid access token', 500

  title = request.form.get('title', None)
  if not title:
      return 'no title found', 500

  summary = request.form.get('summary', None)
  if not summary:
      return 'no summary found', 500

  content = request.form.get('content', None)
  if not content:
      return 'no content found', 500

  content = markdown2html(content)
  pub_time = request.form.get('pub_time', None)
  if pub_time:
      pub_time = datetime.strptime(pub_time, app.config['TIME_FORMAT'])

  tags = request.form.getlist('tags')

  create_article(title, summary, content, pub_time, tags)
  return '', 200
