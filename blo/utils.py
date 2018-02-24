#coding=utf8

import markdown
from datetime import datetime


def markdown2html(mdtext):
    return markdown.markdown(mdtext)

def load_content(name):
    with open('{}.md'.format(name), 'r', encoding='utf-8') as f:
        mdtext = f.read()
    return markdown2html(mdtext)
