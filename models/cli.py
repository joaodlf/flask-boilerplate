from peewee import *

from models import BaseModel


class Cli(BaseModel):
    id = PrimaryKeyField()
    dt_created = DateTimeField()
    dt_finish = DateTimeField(null=True)
    dt_start = DateTimeField(null=True)
    name = CharField()
    pid = IntegerField()

    class Meta:
        db_table = "cli"
