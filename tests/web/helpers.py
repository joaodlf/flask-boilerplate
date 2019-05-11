from functools import wraps

from playhouse.postgres_ext import PostgresqlDatabase

from config import SQL_DATABASE, SQL_HOST, SQL_PASSWORD, SQL_USER


def with_test_db(models: tuple):
    def decorator(func):
        @wraps(func)
        def test_db_closure(*args, **kwargs):
            test_db = PostgresqlDatabase(
                SQL_DATABASE, user=SQL_USER, password=SQL_PASSWORD, host=SQL_HOST
            )
            with test_db.bind_ctx(models):
                test_db.create_tables(models)
                try:
                    func(*args, **kwargs)
                finally:
                    test_db.drop_tables(models)

        return test_db_closure

    return decorator
