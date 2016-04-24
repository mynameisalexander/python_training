# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="update")
    group.id = random_group.id
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    i = 0
    for x in old_groups:
        if x.id == random_group.id:
            old_groups[i] = group
        i += 1
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="update"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)