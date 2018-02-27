#coding=utf8

from datetime import datetime
from . import db


articles_tags = db.Table(
    'articles_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id')))


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    summary = db.Column(db.String(300))
    content = db.Column(db.Text)
    pub_time = db.Column(db.DateTime, default=datetime.now)
    read_times = db.Column(db.Integer, default=1)
    tags = db.relationship('Tag',
                           secondary=articles_tags,
                           backref=db.backref('articles', lazy='dynamic'))

    def __init__(self, title, summary, content, pub_time=None):
        self.title = title
        self.summary = summary
        self.content = content
        if pub_time:
            self.pub_time = pub_time

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return self

    def add_read(self):
        if self.read_times == None:
            self.read_times = 1
        print(self.read_times)
        self.read_times = self.read_times + 1
        self.save()

    def __str__(self):
        return self.title


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name.lower()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


def _get_tag(name):
    name = name.lower()
    tag = db.session.query(Tag).filter(Tag.name==name).first()
    if not tag:
        tag = Tag(name)
        tag.save()
    return tag


def create_article(title, summary, content, pub_time=None, tagnames=[]):
    article = Article(title, summary, content, pub_time)
    for tagname in tagnames:
        tag = _get_tag(tagname.lower())
        article.tags.append(tag)
    article.save()
    return article

def delete_article(title):
    a = db.session.query(Article).filter(Article.title==title).first()
    if a is None:
        return "Article doesn't exsit."
    a.delete()
    a = db.session.query(Article).filter(Article.title==title).first()
    if a:
        return "delete failed."
    else:
        return "delete success."