import peewee
import pendulum
from peewee import *

from models import InetField, ModelBase


class ApiIpWhitelist(ModelBase):
    comment = CharField(null=True)
    dt_created = DateTimeField(default=pendulum.now())
    ip_address = InetField()

    class Meta:
        table_name = "api_ip_whitelist"

    @staticmethod
    def is_valid_ip(ip_address: str):
        """ Validates a single IP (i.e. is it in the database?). """
        # Check ip.
        try:
            valid = ApiIpWhitelist.select().where(ApiIpWhitelist.ip_address == ip_address).get()
        except ApiIpWhitelist.DoesNotExist:
            valid = False

        # Check ip range.
        if not valid:
            try:
                valid = ApiIpWhitelist.raw(
                    "SELECT * FROM api_ip_whitelist WHERE ip_address >> %s::inet;", ip_address
                ).execute()
            except peewee.DataError:
                valid = False

        if valid:
            return True

        return False
