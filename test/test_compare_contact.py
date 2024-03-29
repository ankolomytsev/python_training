import re
from random import randrange
from model.contact import Contact


def test_contact_data_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_contact_data_on_home_page_with_db(app, db):
    contact_from_db = db.get_contact_list()
    for c in contact_from_db:
        c.all_phones_from_home_page = merge_phones_like_on_home_page(c)
        c.all_emails_from_home_page = merge_emails_like_on_home_page(c)

    assert sorted(contact_from_db, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.work, contact.mobile, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "", map(lambda x: clear(x),
                                      filter(lambda x: x is not None,
                                             [contact.email, contact.email2, contact.email3]))))
