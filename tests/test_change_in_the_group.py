
from model.group import Group
from random import randrange

def test_change_in_the_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New one"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="changed header")
    group.id = old_groups[index].id
    app.group.change_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_change_in_the_group_name(app):
#   if app.group.count() == 0:
    #        app.group.create(Group(name="New one"))
    #    old_groups = app.group.get_group_list()
    #  app.group.change_group(Group(name="changed name"))
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)