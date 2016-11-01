from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("nowy wpis").click()

    def open_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("strona główna").click()

    def add(self, contact):
        wd = self.app.wd
        self.open_new_contact_form()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
            wd.find_element_by_xpath(contact.bday).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath(contact.bmonth).click()
        self.change_field_value("byear", contact.birthyear)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[19]").is_selected():
            wd.find_element_by_xpath(contact.aday).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath(contact.amonth).click()
        self.change_field_value("ayear", contact.annyear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.privatephone)
        self.change_field_value("notes", contact.comments)



    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd=self.app.wd
        self.open_homepage()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_homepage()
        self.contact_cache = None

    def change_contact(self):
        wd = self.app.wd
        self.change_contact_by_index(0)

    def change_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_index(index)
        contact_row = wd.find_elements_by_name("entry")[index]
        cell = contact_row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        self.fill_contact_form(contact)
        wd.find_element_by_css_selector("input[name='update']").click()
        self.return_to_homepage()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("strona główna").click()

    def count_contact(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                text1 = cells[1].text
                text2 = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(firstname= text2, lastname= text1, id = id))
            return list(self.contact_cache)


