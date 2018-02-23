# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(firstname="Emme", middlename="Anne", lastname="Imme", nickname="Onne", title="Engineer",
                        company="Engineering", address="Doscoe 6 Wisconsin", home="111 111 111",
                        mobile="222 222 222", work="333 333 333", fax="546 789 876",
                        email="kooll@anne.com", email2="loook@mo.com", email3="inne@mol.com",
                        homepage="zaggfa.co.uk", address2="Selby 72", phone2="555 555 555", notes="Chief Engineer"))
    new_contacts = app.contact.get_contact_list()
    print(old_contacts)
    print(new_contacts)
    assert (len(old_contacts) + 1) == len(new_contacts)


def test_add__empty_contact(app):
    app.contact.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                        company="", address="", home="",
                        mobile="", work="", fax="",
                        email="", email2="", email3="",
                        homepage="", address2="",
                        phone2="", notes=""))

