#!/usr/bin/env python
#coding=utf8

""" 
A simple script for publishing articles written in markdown.
"""


import argparse
import json
from io import StringIO
from io import BytesIO
import re
import requests
import yaml
import markdown
from lxml import html


def _get_file(path):
    return open(path)


def _gen_summary(mdtext, n=360):
    htmltext = markdown.markdown(mdtext)
    tree = html.fromstring(htmltext)
    node = tree.xpath('.')[0]
    text = re.sub(r'\s+', ' ', node.text_content()).strip()
    return text[:n] + ' ...'


def publish(stream, api, token):
    """ Publishing a new article from `stream`"""

    headers = []
    for line in stream:
        if not line:
            break
        line = line.rstrip()
        headers.append(line)
        if line == '...':
            break

    cfg = yaml.load(StringIO('\n'.join(headers)))   # 生成一个字典
    print(cfg)
    if not cfg:
        raise ValueError('no valid yaml config informations')
    if 'title' not in cfg:
        raise ValueError('no title found')
    if 'tags' in cfg and not isinstance(cfg['tags'], list):
        raise ValueError('invalid tags: it should be list')

    bodies = []
    for line in stream:
        bodies.append(line.rstrip())
    content = '\n'.join(bodies).strip()
    if not content:
        raise ValueError('no content found')

    print(bodies)
    data = {
        'token': token,
        'title': cfg['title'],
        'summary': cfg.get('summary', None) or _gen_summary(content),
        'content': content,
    }
    if 'tags' in cfg:
        data['tags'] = cfg['tags']
    if 'pub_time' in cfg:
        data['pub_time'] = cfg['pub_time']

    r = requests.post(api, data=data)
    assert r.status_code == 200, r.content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='markdown file path/url')
    parser.add_argument('-a', '--api', help='api address')
    parser.add_argument('-t', '--token', help='access token')
    args = parser.parse_args()

    if not args.path or not args.api or not args.token:
        parser.print_help()
        # print(dir(parser))
        return

    stream = _get_file(args.path)
    # print(stream)
    publish(stream, args.api, args.token)


if __name__ == '__main__':
    # print("http.bai.com".startswith('http'))
    main( )
