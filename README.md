Publish Articles
================

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

Modify the value of *TOKEN* in [config.py](config.py). 
And use the script `publish.py` to publish articles.

````
$ python publish.py -a http://127.0.0.1:5000/publish -p edit.md -t YOURTOKEN
````
