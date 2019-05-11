from models.api_ip_whitelist import ApiIpWhitelist
from tests.web import testing_app
from tests.web.helpers import with_test_db


@with_test_db((ApiIpWhitelist,))
def test_general_ping_success():
    ApiIpWhitelist.create(ip_address="127.0.0.1")

    response = testing_app.get("/api/general/ping")
    assert response.status_code == 200


@with_test_db((ApiIpWhitelist,))
def test_general_ping_error():
    ApiIpWhitelist.create(ip_address="1.0.0.1")

    response = testing_app.get("/api/general/ping")
    assert response.status_code == 403
