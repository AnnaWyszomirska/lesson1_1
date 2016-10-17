
from model.group import Group

def test_change_in_the_group_header(app):
    app.group.change_group(Group(header="changed header"))




def test_change_in_the_group_name(app):
    app.group.change_group(Group(name="changed name"))