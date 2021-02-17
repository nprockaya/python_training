from Fixtures.application_for_groups import AppGroup
from Fixtures.application_for_contacts import AppContact
import pytest


@pytest.fixture()
def app(request):
    fixture = AppGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture()
def app(request):
    fixture = AppGroup()
    request.addfinalizer(fixture.destroy)
    return fixture
