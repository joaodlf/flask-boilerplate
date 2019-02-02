from peewee import Field, Model, PostgresqlDatabase

from config import SQL_DATABASE, SQL_HOST, SQL_PASSWORD, SQL_PORT, SQL_USER

database = PostgresqlDatabase(SQL_DATABASE,
                              user=SQL_USER,
                              password=SQL_PASSWORD,
                              host=SQL_HOST,
                              port=SQL_PORT)


class ModelBase(Model):
    class Meta:
        database = database


class InetField(Field):
    field_type = "inet"
