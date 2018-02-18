from peewee import Model, PostgresqlDatabase

from config import SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE, SQL_PORT

database = PostgresqlDatabase(SQL_DATABASE,
                              user=SQL_USER,
                              password=SQL_PASSWORD,
                              host=SQL_HOST,
                              port=SQL_PORT)


class BaseModel(Model):
    class Meta:
        database = database
