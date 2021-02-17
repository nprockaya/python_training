from Fixtures.application_for_groups import AppGroup
from Fixtures.application_for_contacts import AppContact
import pytest


@pytest.fixture(scope="session")
def appgroup(request):
    fixture = AppGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture()
def appcontact(request):
    fixture = AppContact()
    request.addfinalizer(fixture.destroy)
    return fixture
