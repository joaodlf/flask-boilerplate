from peewee import *

from models import ModelBase


class Cli(ModelBase):
    id = AutoField()
    dt_created = DateTimeField()
    dt_finish = DateTimeField(null=True)
    dt_start = DateTimeField(null=True)
    name = CharField()
    pid = IntegerField()

    class Meta:
        table_name = "cli"
