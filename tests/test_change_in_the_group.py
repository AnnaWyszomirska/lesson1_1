
from model.group import Group

def test_change_in_the_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.change_group(Group(header="changed header"))
    app.session.logout()



def test_change_in_the_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.change_group(Group(name="changed name"))
    app.session.logout()