from Fixtures.application import Application
import pytest


@pytest.fixture(scope="session", autouse=True)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

