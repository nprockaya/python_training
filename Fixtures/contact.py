from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, appcontact):
        self.app = appcontact

    def open_contact_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        #wd.find_elements_by_id("content")

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_creation_page()
        # init creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.return_to_homepage()

    def fill_contact_form(self, contact):
        self.fill_name(contact)
        self.fill_middle_name(contact)
        self.fill_last_name(contact)
        self.fill_nickname(contact)
        self.fill_title(contact)
        self.fill_company(contact)
        self.fill_address(contact)
        self.fill_home_phone(contact)
        self.fill_mobile_phone(contact)
        self.fill_work_phone(contact)
        self.fill_fax(contact)
        self.fill_email(contact)
        self.fill_email2(contact)
        self.fill_email3(contact)
        self.fill_homepage(contact)
        self.fill_bday(contact)
        self.fill_aday(contact)
        self.fill_secondary_address(contact)
        self.fill_secondary_home(contact)
        self.fill_secondary_notes(contact)

    def fill_name(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)

    def fill_middle_name(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)

    def fill_last_name(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)

    def fill_nickname(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

    def fill_title(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)

    def fill_company(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)

    def fill_address(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

    def fill_home_phone(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)

    def fill_mobile_phone(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)

    def fill_work_phone(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)

    def fill_fax(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)

    def fill_email(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

    def fill_email2(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)

    def fill_email3(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)

    def fill_homepage(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

    def fill_bday(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath("//option[@value='" + contact.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath("//option[@value='" + contact.bmonth + "']")
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)

    def fill_aday(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_xpath("//option[@value='" + contact.aday + "']").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_xpath("//option[@value='" + contact.amonth + "']").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def fill_secondary_address(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)

    def fill_secondary_home(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_home)

    def fill_secondary_notes(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        first_element = wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[1]")
        first_element.click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.return_to_homepage()
        # select first group
        self.select_first_contact()
        # click edit
        wd.find_element_by_xpath("(//img[@alt='Edit'])[2]").click()
        wd.find_element_by_xpath("//form[@action='edit.php']").click()
        # edit fields
        self.fill_contact_form(contact)
        # submit edit
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_homepage()
        # select first group
        self.select_first_contact()
        # click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept
        wd.switch_to_alert().accept()
        self.return_to_homepage()

    def count_contacts(self):
        wd = self.app.wd
        self.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))


    # def select_second_contact(self):
    #     wd = self.app.wd
    #     for element in wd.find_elements_by_name("selected[]"):
    #         if element == wd.find_element_by_id("29"):
    #             pass  # no action required
    #         else:
    #             element.click()
    #             break
