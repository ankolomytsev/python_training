# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    app.open_home_page()
    app.contact.edit_first_contact(Contact(firstname='qwerty'))

