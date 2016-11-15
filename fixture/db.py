import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database = name, user = user, password =password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list ")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id = str(id), name = name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname, home, mobile, work, phone2, email, email2, email3, address from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, lastname, firstname, home, address, email, email2, email3, mobile, work, privatephone) = row
                list.append(Contact(firstname = firstname, lastname= lastname, id = str(id), home =home, address= address, email=email, email2=email2, email3= email3,
                       mobile=mobile, work = work, privatephone=privatephone ))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()


