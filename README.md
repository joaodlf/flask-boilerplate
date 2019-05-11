# flask-boilerplate

A boilerplate project for Flask+CLI applications. More information [here](https://joaodlf.com/python-for-the-web-in-2019.html#python-for-the-web-in-2019) (original blog post [here](https://joaodlf.com/python-for-the-web.html)).

You must create a `config.py` file in the `config` dir of the project (an example file is provided)

## Development

The project is currently developed under Python **3.7**. I recommend [pyenv](https://github.com/pyenv/pyenv)
to manage your Python environments. A `.python-version` file is supplied at the root of the project.

You'll need a new virtualenv:

```
$ python -m venv env
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

I prefer to run uwsgi in development and production. Running a local server is as easy as:

```
$ uwsgi --ini web/uwsgi/development.ini --http :8080
```

You should now be able to navigate to http://127.0.0.1:8080/

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
$ pytest -vs
```

**Note:** You will need to setup a test database in your `config/test_config.py` file.