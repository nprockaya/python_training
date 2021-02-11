# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from contact_class import Contact
import unittest

class test_Add_Contact (unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
    
    def test_add_contact_normal(self):
        # open "address book"
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_contact_creation_page(wd)
        self.contact_creation(wd, Contact(first_name_value="Firstname", middle_name_value="Middlename", last_name_value="Lastname", nickname_value="Nickname", title_value="Title", company_value="Company", address_value="123456, address_city, address_street, address_home", home_phone_value="123456_home_phone", mobile_phone_value="123456_mobile_phone", work_phone_value="123456_work_phone", fax_value="123456_fax", email_value="1@mail.com", email2_value="2@mail.com", email3_value="3@mail.com", homepage_value="https://home_page.com", secondary_address_value="Second address", secondary_home_value="Second home", secondary_notes_value="Notes"))
        # submit contact creation and return to home page
        self.submit_contact_creation(wd)
        self.return_to_homepage(wd)
        self.logout(wd)

    def login(self, wd, user_name, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def open_contact_creation_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def contact_creation(self, wd, contact):
        # init creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_name(contact, wd)
        self.fill_middle_name(contact, wd)
        self.fill_last_name(contact, wd)
        self.fill_nickname(contact, wd)
        self.fill_title(contact, wd)
        self.fill_company(contact, wd)
        self.fill_address(contact, wd)
        self.fill_home_phone(contact, wd)
        self.fill_mobile_phone(contact, wd)
        self.fill_work_phone(contact, wd)
        self.fill_fax(contact, wd)
        self.fill_email(contact, wd)
        self.fill_email2(contact, wd)
        self.fill_email3(contact, wd)
        self.fill_homepage(contact, wd)
       # self.fill_bday(wd)
       # self.fill_aday(wd)
        self.fill_secondary_address(contact, wd)
        self.fill_secondary_home(contact, wd)
        self.fill_secondary_notes(contact, wd)

    def fill_name(self, contact, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)

    def fill_middle_name(self, contact, wd):
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)

    def fill_last_name(self, contact, wd):
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)

    def fill_nickname(self, contact, wd):
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

    def fill_title(self, contact, wd):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)

    def fill_company(self, contact, wd):
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)

    def fill_address(self, contact, wd):
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

    def fill_home_phone(self, contact, wd):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)

    def fill_mobile_phone(self, contact, wd):
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)

    def fill_work_phone(self, contact, wd):
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)

    def fill_fax(self, contact, wd):
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)

    def fill_email(self, contact, wd):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

    def fill_email2(self, contact, wd):
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)

    def fill_email3(self, contact, wd):
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)

    def fill_homepage(self, contact, wd):
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

    # def fill_bday(self, wd):
    #    wd.find_element_by_name("bday").click()
    #    Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
    #    wd.find_element_by_xpath("//option[@value='1']").click()
    #    wd.find_element_by_name("bmonth").click()
    #    Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
    #    wd.find_element_by_xpath("//option[@value='January']").click()
    #    wd.find_element_by_name("byear").click()
    #    wd.find_element_by_name("byear").clear()
    #    wd.find_element_by_name("byear").send_keys("2000")

    # def fill_aday(self, wd):
    #    Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
    #    wd.find_element_by_xpath("(//option[@value='2'])[2]").click()
    #    wd.find_element_by_name("amonth").click()
    #    Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
    #    wd.find_element_by_xpath("(//option[@value='January'])[2]").click()
    #    wd.find_element_by_name("ayear").click()
    #    wd.find_element_by_name("ayear").clear()
    #    wd.find_element_by_name("ayear").send_keys("2020")

    def fill_secondary_address(self, contact, wd):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)

    def fill_secondary_home(self, contact, wd):
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_home)

    def fill_secondary_notes(self, contact, wd):
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)

    def submit_contact_creation (self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()