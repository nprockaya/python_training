class GroupHelper:

    def __init__(self, appgroup):
        self.appg = appgroup

    def open_groups_page(self):
        wd = self.appg.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.appg.wd
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
        wd = self.appg.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)

    def fill_group_header(self, group):
        wd = self.appg.wd
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_xpath("//form[@action='/addressbook/group.php']").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)

    def fill_group_footer(self, group):
        wd = self.appg.wd
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def return_to_groups_page(self):
        wd = self.appg.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.appg.wd
        wd.find_element_by_link_text("groups").click()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()