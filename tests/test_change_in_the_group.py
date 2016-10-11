
from model.group_change import GroupChange

def test_change_in_the_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change_group(GroupChange(name1="changed name", header1="changed header", footer1="changed footer"))
    app.session.logout()