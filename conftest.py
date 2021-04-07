from Fixtures.application import Application
import pytest
import json
import os.path
import importlib

fixture = None
target = None


@pytest.fixture()
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as open_file:
            target = json.load(open_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["base_url"])
    fixture.session.ensure_login(target["user_name"], target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def final():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(final)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_form_module(module):
    return importlib.import_module("Data.%s" % module).test_data
