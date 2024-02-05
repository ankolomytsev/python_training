from model.contact import Contact
from model.group import Group
import random


def test_add_some_contact_to_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact_for_adding = random.choice(db.get_contact_list())
    group_for_adding = random.choice(db.get_group_list())
    old_contacts_in_selected_group = db.get_contacts_in_group(group_for_adding)
    app.contact.add_contact_to_group(contact_for_adding.id, group_for_adding.name)
    new_contacts_in_selected_group = db.get_contacts_in_group(group_for_adding)
    old_contacts_in_selected_group.append(contact_for_adding)
    assert sorted(old_contacts_in_selected_group, key=Contact.id_or_max) == sorted(new_contacts_in_selected_group, key=Contact.id_or_max)
