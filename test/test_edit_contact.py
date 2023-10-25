# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")

    #Подготовка дефолтного контакта для редактирования
    app.contact.create(Contact())

    app.contact.edit_first_contact(Contact(firstname='123'))
    app.session.logout()
