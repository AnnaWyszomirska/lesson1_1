class GroupHelper:
    def __init__(self):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("grupy").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("grupa lesson1")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select//option[1]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()