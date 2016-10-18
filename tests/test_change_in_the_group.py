
from model.group import Group

def test_change_in_the_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New one"))
    app.group.change_group(Group(header="changed header"))




def test_change_in_the_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New one"))
    app.group.change_group(Group(name="changed name"))