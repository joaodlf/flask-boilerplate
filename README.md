# flask-boilerplate

A boilerplate project for Flask+CLI applications. More information [here](https://joaodlf.com/python-for-the-web.html).

You must create a `config.py` file at the root of the project (an example file is provided in `config_example.py`)

## Development

This project was built on Python **3.6** (You should be fine with any Python 3.6.* version).

You'll need a new virtualenv:

```
$ python3 -m venv env
$ . env/bin/activate

```

Install requirements via pip:

```
$ pip install -r requirements.txt
```

It's also recommended to set your PYTHONPATH to the root of the project:

```
$ export PYTHONPATH=$(pwd)
```

### Web

uwsgi is used in production *and* development. Running a local server is as easy as:

```
$ sudo uwsgi --ini web/uwsgi/development.ini
```

(tip: You can modify the default port via the **development.ini** file)

You should now be able to navigate to http://127.0.0.1:80/

### CLI

A CLI example can be run via:

```
$ python cli/example.py example
```

## Database

Postgres is the supported RDBM.

To import the database, run:

```
$ psql <project_name> < dev/schema.sql
```