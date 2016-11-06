from model.contact import Contact
import re

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
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
            #wd.find_element_by_xpath(contact.bday).click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            #wd.find_element_by_xpath(contact.bmonth).click()
        #self.change_field_value("byear", contact.birthyear)
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[19]").is_selected():
            #wd.find_element_by_xpath(contact.aday).click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            #wd.find_element_by_xpath(contact.amonth).click()
        self.change_field_value("ayear", contact.annyear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.privatephone)
        self.change_field_value("notes", contact.comments)



    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd=self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_homepage()
        self.contact_cache = None

    def change_contact(self):
        wd = self.app.wd
        self.change_contact_by_index(0)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        contact_row = wd.find_elements_by_name("entry")[index]
        cell = contact_row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def change_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
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
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        contact_row = wd.find_elements_by_name("entry")[index]
        cell = contact_row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                text1 = cells[1].text
                text2 = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname= text2, lastname= text1, id = id, address= address,
                                                  all_emails_form_home_page= all_emails,  all_phones_from_home_page = all_phones))
        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        privatephone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname = firstname, lastname= lastname, id = id, home =home, address= address, email=email, email2=email2, email3= email3,
                       mobile=mobile, work = work, privatephone=privatephone )

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        privatephone = re.search("P: (.*)", text).group(1)
        return Contact(home=home,mobile=mobile, work=work, privatephone=privatephone)

