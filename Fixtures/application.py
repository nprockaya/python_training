from selenium import webdriver
from Fixtures.session import SessionHelper
from Fixtures.group import GroupHelper
from Fixtures.contact import ContactHelper

class Application:
    def __init__(self, browser="firefox", base_url="http://localhost/addressbook/"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url=base_url

    def open_homepage_group(self):
        wd = self.wd
        wd.get(self.base_url)

    def open_homepage_contact(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

