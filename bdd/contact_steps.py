from pytest_bdd import given, when, then
from pytest_bdd.parsers import parse
from fixture.contact import Contact
import random


@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()


@given(
    parse('a contact with {firstname}, {lastname}'),
    target_fixture='new_contact'
)
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I add the contact to the list', target_fixture='add_new_contact')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then(
    'the new contact list is equal to the old list with the added contact',
    target_fixture='verify_contact_added'
)
def verify_contact_added(db, contact_list, new_contact, app, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="test"))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list', target_fixture='delete_contact')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then(
    'the new contact list is equal to the old list without the deleted contact',
    target_fixture='verify_contact_deleted'
)
def verify_contact_deleted(
        db, app, non_empty_contact_list, random_contact, check_ui
):
    old_contacts = non_empty_contact_list
    assert len(non_empty_contact_list) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max)


@given(
    parse('an edited contact with {firstname}, {lastname}'),
    target_fixture='contact_for_editing'
)
def contact_for_editing(firstname, lastname, random_contact):
    return Contact(firstname=firstname, lastname=lastname, id=random_contact.id)


@when('I edit the contact in the list', target_fixture='edit_contact')
def edit_contact(app, random_contact, contact_for_editing):
    app.contact.edit_contact_by_id(random_contact.id, contact_for_editing)


@then(
    'the new contact list is equal to the old list with the edited contact',
    target_fixture='verify_contact_edited'
)
def verify_contact_edited(
        app, non_empty_contact_list, random_contact,
        contact_for_editing, check_ui
):
    old_contacts = non_empty_contact_list
    old_contacts.remove(random_contact)
    old_contacts.append(contact_for_editing)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max)
