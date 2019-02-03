# flask-boilerplate

A boilerplate project for Flask+CLI applications. More information [here](https://joaodlf.com/python-for-the-web.html).

You must create a `config.py` file in the `config` dir of the project (an example file is provided)

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
$ python cli/example.py
```

## Database

Postgres 10 is the supported RDBM.

### Migrations
[Flyway](https://flywaydb.org/) is required for db migrations. Migration files are located in
the `migrations` dir.

If you are on macos, flyway can be installed via brew:
```
$ brew install flyway
```

If setting up a new database, create a `flyway.conf` file at the root
of the project:

```
flyway.url=jdbc:postgresql://<hostname>:<port>/<database>
flyway.user=<user>
flyway.password=<password>
flyway.locations=filesystem:./
```

You should now be ready to run `flyway baseline` and `flyway migrate`.

## Tests

Basic tests are supplied in the `tests` dir, which can be run via pytest:

```
$ pytest -vs -p no:warnings
```