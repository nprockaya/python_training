from Fixtures.application import Application
from Fixtures.db import DbFixture
import pytest
import jsonpickle
import json
import os.path
import importlib

fixture = None
target = None


@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["base_url"])
    fixture.session.ensure_login(web_config["user_name"], web_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def final():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(final)
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host_value=db_config["host"], name_value=db_config["name"], user_value=db_config["user"],
                          password_value=db_config["password"])

    def final():
        dbfixture.destroy()

    request.addfinalizer(final)
    return dbfixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

@pytest.fixture()
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(module):
    return importlib.import_module("Data.%s" % module).test_data


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as open_file:
            target = json.load(open_file)
    return target
