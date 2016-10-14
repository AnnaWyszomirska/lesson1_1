
from model.group import Group

def test_change_in_the_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change_group(Group(name="changed name", header="changed header", footer="changed footer"))
    app.session.logout()