from model.group import Group
from random import randrange
import random


def test_edit_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = Group(name="QAZXSW")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_first_group_header(app):
#      if app.group.count() == 0:
#          app.group.create(Group(name="test"))
#      old_groups = app.group.get_group_list()
#      app.group.edit_first_group(Group(header="new header"))
#      new_groups = app.group.get_group_list()
#      assert len(old_groups) == len(new_groups)
