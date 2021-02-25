from selenium import webdriver
from Fixtures.session import SessionHelper
from Fixtures.group import GroupHelper
from Fixtures.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        #self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_homepage_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_homepage_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False