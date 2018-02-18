import peewee
from peewee import *

from models import BaseModel


class ApiIpWhitelist(BaseModel):
    comment = CharField(null=True)
    dt_created = DateTimeField()
    ip_address = CharField()  # inet field, peewee does not support this type!

    class Meta:
        db_table = "api_ip_whitelist"

    @staticmethod
    def is_valid_ip(ip_address: str):
        """ Validates a single IP (i.e. is it in the database?). """
        # Check ip.
        try:
            valid = ApiIpWhitelist.select().where(ApiIpWhitelist.ip_address == ip_address).get()
        except ApiIpWhitelist.DoesNotExist:
            valid = False

        if not valid:
            # Check ip range.
            try:
                valid = ApiIpWhitelist.raw(
                    "SELECT * FROM api_ip_whitelist WHERE ip_address >> %s::inet;", ip_address
                ).execute()
            except peewee.DataError:
                valid = False

        if valid:
            return True

        return False
