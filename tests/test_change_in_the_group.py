
from model.group import Group

def test_change_in_the_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New one"))
    old_groups = app.group.get_group_list()
    group = Group(header="changed header")
    group.id = old_groups[0].id
    app.group.change_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_change_in_the_group_name(app):
#   if app.group.count() == 0:
    #        app.group.create(Group(name="New one"))
    #    old_groups = app.group.get_group_list()
    #  app.group.change_group(Group(name="changed name"))
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)