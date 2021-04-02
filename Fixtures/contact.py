from selenium.webdriver.support.ui import Select
from Models.contact_class import Contact
from time import sleep


class ContactHelper:

    def __init__(self, appcontact):
        self.app = appcontact

    def open_contact_creation_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_creation_page()
        # init creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.return_to_homepage()
        self.contact_cache = None

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
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_id("search_count")) > 0):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//table/tbody/tr[" + str(index + 2) + "]/td[1]/input").click()

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.return_to_homepage()
        # click edit
        wd.find_element_by_xpath("(//table/tbody/tr[" + str(index + 2) + "]//img[@alt='Edit'])").click()
        # edit fields
        self.fill_contact_form(contact)
        # submit edit
        wd.find_element_by_xpath("(//input[@name='update'])").click()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_homepage()
        # select first contact
        self.select_contact_by_index(index)
        # click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept
        wd.switch_to_alert().accept()
        # waiting for confirmation
        wd.find_element_by_xpath("//div[@class='msgbox']")
        self.return_to_homepage()
        self.contact_cache = None

    def count_contacts(self):
        wd = self.app.wd
        self.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_homepage()
            self.contact_cache = []
            for contacts_rows in wd.find_elements_by_name("entry"):
                contacts_cells = contacts_rows.find_elements_by_tag_name("td")
                local_contact_firstname = contacts_cells[2].text
                local_contact_lastname = contacts_cells[1].text
                local_contact_id = contacts_cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = contacts_cells[5].text.splitlines()
                self.contact_cache.append(
                    Contact(first_name_value=local_contact_firstname, last_name_value=local_contact_lastname,
                            contact_id_value=local_contact_id, home_phone_value=all_phones[0],
                            mobile_phone_value=all_phones[1], work_phone_value=all_phones[2],
                            secondary_home_value=all_phones[3]))
        return list(self.contact_cache)

    def view_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_homepage()
        # click view
        wd.find_element_by_xpath("(//table/tbody/tr[" + str(index + 2) + "]//img[@alt='Edit'])").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.view_contact_by_index(index)
        # person data
        first_name_ep = wd.find_element_by_name("firstname").get_attribute("value")
        last_name_ep = wd.find_element_by_name("lastname").get_attribute("value")
        contact_id_ep = wd.find_element_by_name("id").get_attribute("value")
        # phones
        home_phone_ep = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone_ep = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone_ep = wd.find_element_by_name("work").get_attribute("value")
        secondary_home_ep = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name_value=first_name_ep, last_name_value=last_name_ep,
                       contact_id_value=contact_id_ep, home_phone_value=home_phone_ep,
                       work_phone_value=work_phone_ep, mobile_phone_value=mobile_phone_ep,
                       secondary_home_value=secondary_home_ep)
