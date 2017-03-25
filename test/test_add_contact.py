# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Emme", middlename="Anne", lastname="Imme", nickname="Onne", title="Engineer",
                        company="Engineering", address="Doscoe 6 Wisconsin", homephone="111 111 111",
                        mobilephone="222 222 222", workphone="333 333 333", faxnumber="546 789 876",
                        email1="kooll@anne.com", email2="loook@mo.com", email3="inne@mol.com",
                        website="zaggfa.co.uk", address2="Selby 72",
                        homephone2="555 555 555", notes="Chief Engineer"))
    app.session.logout()


def test_add__empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                        company="", address="", homephone="",
                        mobilephone="", workphone="", faxnumber="",
                        email1="", email2="", email3="",
                        website="", address2="",
                        homephone2="", notes=""))
    app.session.logout()
