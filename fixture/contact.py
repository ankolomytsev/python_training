from selenium.webdriver.support.select import Select
from model.contact import Contact
from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element("link text", "add new").click()
        self.fill_contact_form(contact)
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name", "selected[]")[index].click()
        wd.find_element("xpath", "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element("css selector", "input[value='%s']" % id).click()
        wd.find_element("xpath", "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0, new_contact_data)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_elements("xpath", "//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element("name", "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        xpath = f'edit.php?"id={id}"]'
        wd.find_element(By.XPATH, "//*[@id='%s']/../..//*[@title='Edit']" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element("name", "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_text_field_value("firstname", contact.firstname)
        self.change_text_field_value("middlename", contact.middlename)
        self.change_text_field_value("lastname", contact.lastname)
        self.change_text_field_value("nickname", contact.nickname)
        self.change_text_field_value("photo", contact.photo)
        self.change_text_field_value("title", contact.title)
        self.change_text_field_value("company", contact.company)
        self.change_text_field_value("address", contact.address)
        self.change_text_field_value("home", contact.home)
        self.change_text_field_value("mobile", contact.mobile)
        self.change_text_field_value("workphone", contact.workphone)
        self.change_text_field_value("fax", contact.fax)
        self.change_text_field_value("email", contact.email)
        self.change_text_field_value("email2", contact.email2)
        self.change_text_field_value("email3", contact.email3)
        self.change_text_field_value("homepage", contact.homepage)
        self.change_dropdown_field_value("bday", contact.bday)
        self.change_dropdown_field_value("bmonth", contact.bmonth)
        self.change_text_field_value("byear", contact.byear)
        self.change_dropdown_field_value("aday", contact.aday)
        self.change_dropdown_field_value("amonth", contact.amonth)
        self.change_text_field_value("ayear", contact.ayear)
        self.change_text_field_value("address2", contact.address2)
        self.change_text_field_value("phone2", contact.phone2)
        self.change_text_field_value("notes", contact.notes)

    def change_text_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def change_dropdown_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element("name", field_name)).select_by_visible_text(value)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements("name", "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements("name", "entry"):
                id = element.find_element("name", "selected[]").get_attribute("value")
                firstname = element.find_element("xpath", "td[3]").text
                lastname = element.find_element("xpath", "td[2]").text
                address = element.find_element("xpath", "td[4]").text
                all_phones = element.find_element("xpath", "td[6]").text
                all_emails = element.find_element("xpath", "td[5]").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements("name", "entry")[index].find_element("xpath", "td[8]").find_element("tag name", "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element("name", "firstname").get_attribute("value")
        lastname = wd.find_element("name", "lastname").get_attribute("value")
        id = wd.find_element("name", "id").get_attribute("value")
        address = wd.find_element("name", "address").get_attribute("value")
        home = wd.find_element("name", "home").get_attribute("value")
        mobile = wd.find_element("name", "mobile").get_attribute("value")
        workphone = wd.find_element("name", "work").get_attribute("value")
        phone2 = wd.find_element("name", "phone2").get_attribute("value")
        email = wd.find_element("name", "email").get_attribute("value")
        email2 = wd.find_element("name", "email2").get_attribute("value")
        email3 = wd.find_element("name", "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, home=home,
                       mobile=mobile, workphone=workphone, phone2=phone2, email=email, email2=email2,
                       email3=email3)
