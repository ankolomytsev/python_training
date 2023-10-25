from selenium.webdriver.support.select import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element("link text", "add new").click()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "middlename").send_keys(contact.middlename)
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("name", "nickname").send_keys(contact.nickname)
        wd.find_element("name", "photo").send_keys(contact.photo)
        wd.find_element("name", "title").send_keys(contact.title)
        wd.find_element("name", "company").send_keys(contact.company)
        wd.find_element("name", "address").send_keys(contact.address)
        wd.find_element("name", "home").send_keys(contact.homephone)
        wd.find_element("name", "mobile").send_keys(contact.mobile)
        wd.find_element("name", "work").send_keys(contact.workphone)
        wd.find_element("name", "fax").send_keys(contact.fax)
        wd.find_element("name", "email").send_keys(contact.email)
        wd.find_element("name", "email2").send_keys(contact.email2)
        wd.find_element("name", "email3").send_keys(contact.email3)
        wd.find_element("name", "homepage").send_keys(contact.homepage)
        Select(wd.find_element("name", "bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element("name", "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element("name", "byear").send_keys(contact.byear)
        Select(wd.find_element("name", "aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element("name", "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element("name", "byear").send_keys(contact.ayear)
        wd.find_element("name", "address2").send_keys(contact.address2)
        wd.find_element("name", "phone2").send_keys(contact.homephone2)
        wd.find_element("name", "notes").send_keys(contact.notes)
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()
        wd.find_element("xpath", "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element("xpath", "/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "middlename").send_keys(contact.middlename)
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("name", "nickname").send_keys(contact.nickname)
        wd.find_element("name", "photo").send_keys(contact.photo)
        wd.find_element("name", "title").send_keys(contact.title)
        wd.find_element("name", "company").send_keys(contact.company)
        wd.find_element("name", "address").send_keys(contact.address)
        wd.find_element("name", "home").send_keys(contact.homephone)
        wd.find_element("name", "mobile").send_keys(contact.mobile)
        wd.find_element("name", "work").send_keys(contact.workphone)
        wd.find_element("name", "fax").send_keys(contact.fax)
        wd.find_element("name", "email").send_keys(contact.email)
        wd.find_element("name", "email2").send_keys(contact.email2)
        wd.find_element("name", "email3").send_keys(contact.email3)
        wd.find_element("name", "homepage").send_keys(contact.homepage)
        Select(wd.find_element("name", "bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element("name", "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element("name", "byear").send_keys(contact.byear)
        Select(wd.find_element("name", "aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element("name", "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element("name", "byear").send_keys(contact.ayear)
        wd.find_element("name", "address2").send_keys(contact.address2)
        wd.find_element("name", "phone2").send_keys(contact.homephone2)
        wd.find_element("name", "notes").send_keys(contact.notes)
        wd.find_element("name", "update").click()
        self.return_to_home_page()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home").click()

