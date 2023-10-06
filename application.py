from selenium import webdriver
from selenium.webdriver.support.select import Select


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element("link text", "groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element("name", "new").click()
        # fill group form
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        wd.find_element("name", "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element("link text", "group page").click()

    def create_contact(self, contact):
        wd = self.wd
        wd.find_element("link text", "add new").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys(contact.middlename)
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("name", "nickname").clear()
        wd.find_element("name", "nickname").send_keys(contact.nickname)
        wd.find_element("name", "photo").clear()
        wd.find_element("name", "photo").send_keys(contact.photo)
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys(contact.title)
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys(contact.company)
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys(contact.address)
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys(contact.homephone)
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys(contact.mobile)
        wd.find_element("name", "work").clear()
        wd.find_element("name", "work").send_keys(contact.workphone)
        wd.find_element("name", "fax").clear()
        wd.find_element("name", "fax").send_keys(contact.fax)
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys(contact.email)
        wd.find_element("name", "email2").clear()
        wd.find_element("name", "email2").send_keys(contact.email2)
        wd.find_element("name", "email3").clear()
        wd.find_element("name", "email3").send_keys(contact.email3)
        wd.find_element("name", "homepage").clear()
        wd.find_element("name", "homepage").send_keys(contact.homepage)
        Select(wd.find_element("name", "bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element("name", "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element("name", "byear").clear()
        wd.find_element("name", "byear").send_keys(contact.byear)
        Select(wd.find_element("name", "aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element("name", "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element("name", "byear").clear()
        wd.find_element("name", "byear").send_keys(contact.ayear)
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys(contact.address2)
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys(contact.homephone2)
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys(contact.notes)
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element("link text", "home page").click()

    def logout(self):
        wd = self.wd
        wd.find_element("link text", "Logout").click()

    def destoy(self):
        self.wd.quit()