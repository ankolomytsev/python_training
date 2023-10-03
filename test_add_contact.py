# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="Vasiliy", lastname="Pupkin"))
        self.return_to_home_page(wd)
        self.logout(wd)
    def open_home_page(self, wd):
        wd.get("https://localhost/addressbook/")
    def login(self, wd, username, password):
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()
    def create_contact(self, wd, contact):
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

    def return_to_home_page(self, wd):
        wd.find_element("link text", "home page").click()

    def logout(self, wd):
        wd.find_element("link text", "Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
