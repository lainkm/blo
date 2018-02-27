---
title: Test
tags:
  - python
  - daily
  - daily2
  - daily3
  - daily4
  - daily5
  - daily6
  - daily7
  - daily8
  - c++
  - java
  - englishword
  - mark
  - hahahahah
...


Test
====

Quick Start
-----------

````
git clone https://github.com/lainkm/blo.git
cd blo
````

#### virtualvenv On Windows:

````
virtualenv venv
venv\Scripts\activate
````

#### virtualvenv On Linux:

````
sudo virtualenv -p /usr/bin/python3.5 venv
source venv/bin/activate
````

#### Requirents

````
sudo pip install -r requirements.txt
````

#### Database

````
sudo python3 manage.py db init
sudo python3 manage.py db migrate
sudo python3 manage.py db upgrade
````

#### Run

````
sudo python3 manage.py runserver
````

Now, visit `http://127.0.0.1:5000` in a browser.


Write articles
--------------

#### [edit](https://raw.githubusercontent.com/lainkm/blo/master/edit.md) markdown file

* **The boundry of meta**('---'and'...')
* **title** (must)

* **summary** (optional)

* **pub_time** (optional)

* **tags** (optional)

  ````
  ---
  title: This is a title
  summary:
    This is a summary
  pub_time: 2017-12-16 21:30:00
  tags:
    - daily
    - python
  ...

  Write the body content here..
  ````


Upload articles
---------------

We provide a simple script to make the publishing work easy. Run `publish.py` to check the help message.

````
$ python publish

usage: publish.py [-h] [-p PATH] [-a API] [-t TOKEN]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  markdown file path/url
  -a API, --api API     api address
  -t TOKEN, --token TOKEN
                        access token
````

You should provide the markdown file(either file-path or raw-url), the target api, and the access token. In this blog system, the publish url is `/publish`. The access token is the value of *TOKEN* in [config.py](config.py). 
**Anyone who know the token could publish articles to your blog system, so keep it secret!!**

After starting the web server locally, you can publish an article like this:

````
$ python publish.py -a http://127.0.0.1:5000/publish -p edit.md -t YOURTOKEN
````
