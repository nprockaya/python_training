# -*- coding: utf-8 -*-
from selenium import webdriver
from group_class import Group
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def test_add_normal_group(self):
        self.login(user_name="admin", password="secret")
        self.group_creation(Group(_name="group_1", _header="group_1", _footer="group_1"))
        self.logout()

    def test_add_empty_group(self):
       self.login(user_name="admin", password="secret")
       self.group_creation(Group(_name="", _header="", _footer=""))
       self.logout()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, user_name, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def group_creation(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_name(group)
        self.fill_group_header(group)
        self.fill_group_footer(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_name(self, group):
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)

    def fill_group_header(self, group):
        wd = self.wd
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_xpath("//form[@action='/addressbook/group.php']").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)

    def fill_group_footer(self, group):
        wd = self.wd
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
