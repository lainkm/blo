Publish Articles
================

Link: [lainly.heroku.com](https://lainly.herokuapp.com/)

Quick Start
-----------


    git clone https://github.com/lainkm/blo.git
    cd blo

#### virtualvenv On Windows:

    virtualenv venv
    venv\Scripts\activate

#### virtualvenv On Linux:

    sudo virtualenv -p /usr/bin/python3.5 venv
    source venv/bin/activate

#### Requirents

    sudo pip install -r requirements.txt

#### Database

    sudo python3 manage.py db init
    sudo python3 manage.py db migrate
    sudo python3 manage.py db upgrade

#### Run

    sudo python3 manage.py runserver

Now, visit `http://127.0.0.1:5000` in a browser.


Write articles ([edit](https://raw.githubusercontent.com/lainkm/blo/master/edit.md) markdown file)
--------------------------------------------------------------------------------------------------

    The boundry of meta ('---'and'...')
    title (must)
    summary (optional)
    pub_time (optional)
    tags (optional)

like:

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


Upload articles
---------------

Modify the value of *TOKEN* in [config.py](config.py). 
And use the script `publish.py` to publish articles.(Use sudo -E to propagate variables)

    export TOKEN=YOURTOKEN
    sudo -E python3 publish.py -a http://127.0.0.1:5000/publish -p edit.md -t YOURTOKEN

or 

    * local.env *
    export TOKEN=YOURTOKEN

    $ source local.env
    $ sudo -E python3 publish.py -a http://127.0.0.1:5000/publish -p edit.md -t YOURTOKEN

and after deploy on heroku(same):


    heroku config:set TOKEN=YOURTOKEN
    sudo python3 publish.py -a https://lainly.herokuapp.com/publish -p edit.md -t YOURTOKEN

delete articles
---------------
use the script `delete.py` (if any space in args`-n`, use "")

    sudo -E python3 delete.py -a http://127.0.0.1:5000/delete -n "Publish Articles" -t YOURTOKEN

edit articles
-------------
\.\.\.


heroku push
-----------

    git add **
    git commit -m "**"

    heroku maintenance:on
    git push heroku master
    heroku run python manage.py db upgrade
    heroku restart
    heroku maintenance:off

TODO
----

    Publish article without a script or user login haddling.
    Publish/edit/delete article via form.(sames that i have to write user auth..)
    Use environment variables(like add .env file) to protect these articles.

