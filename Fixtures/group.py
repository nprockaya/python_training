from Models.group_class import Group


class GroupHelper:

    def __init__(self, appgroup):
        self.app = appgroup

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("New")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def check_group_fields(self, field_name, field_text):
        wd = self.app.wd
        if field_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.check_group_fields("group_name", group.name)
        self.check_group_fields("group_header", group.header)
        self.check_group_fields("group_footer", group.footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("New")) > 0):
            wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # click edit
        wd.find_element_by_name("edit").click()
        # edit fields
        self.fill_group_form(new_group_data)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(_name=text, _id=id))
        return list(self.group_cache)

