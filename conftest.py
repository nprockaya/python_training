from Fixtures.application import Application
import pytest


@pytest.fixture(scope="session", autouse=True)
def app(request):
    fixture = Application()
    fixture.session.login(user_name="admin", password="secret")

    def final():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture
