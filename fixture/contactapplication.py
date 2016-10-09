from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class ContactApplication():
    def __init__(self):
        self.wd = WebDriver(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def destroy(self):
        self.wd.quit()