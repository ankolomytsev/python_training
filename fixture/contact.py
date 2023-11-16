from selenium.webdriver.support.select import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element("link text", "add new").click()
        self.fill_contact_form(contact)
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()
        wd.find_element("xpath", "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.return_to_home_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element("xpath", "/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element("name", "update").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_text_field_value("firstname", contact.firstname)
        self.change_text_field_value("middlename", contact.middlename)
        self.change_text_field_value("lastname", contact.lastname)
        self.change_text_field_value("nickname", contact.nickname)
        self.change_text_field_value("photo", contact.photo)
        self.change_text_field_value("title", contact.title)
        self.change_text_field_value("company", contact.company)
        self.change_text_field_value("address", contact.address)
        self.change_text_field_value("homephone", contact.homephone)
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
        self.change_text_field_value("homephone2", contact.homephone2)
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

