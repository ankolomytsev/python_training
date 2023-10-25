# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")

    #Подготовка дефолтного контакта для удаления
    app.contact.create(Contact())

    app.contact.delete_first_contact()
    app.session.logout()
