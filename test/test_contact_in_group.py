from model.contact import Contact
from model.group import Group
import random


def test_add_random_contact_to_random_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    if len(db.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="test2"))
    contact = random.choice(db.get_contacts_not_in_group(group))
    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group,
                                                                              key=Contact.id_or_max)


def test_remove_random_contact_from_random_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    if len(db.get_contacts_in_group(group)) == 0:
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact, group)
    old_contacts_in_group = db.get_contacts_in_group(group)
    contact_to_remove = random.choice(old_contacts_in_group)
    app.contact.remove_contact_from_group(contact_to_remove, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert contact_to_remove not in new_contacts_in_group
    new_contacts_in_group.append(contact_to_remove)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group,
                                                                              key=Contact.id_or_max)
