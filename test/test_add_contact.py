# -*- coding: utf-8 -*-
import pytest

from fixture.application_2 import Application2
from model.contact import Contact


@pytest.fixture
def app2(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app2):
    app2.login(username="admin", password="secret")
    app2.create_contact(Contact(firstname="Emme", middlename="Anne", lastname="Imme", nickname="Onne", title="Engineer",
                        company="Engineering", address="Doscoe 6 Wisconsin", homephone="111 111 111",
                        mobilephone="222 222 222", workphone="333 333 333", faxnumber="546 789 876",
                        email1="kooll@anne.com", email2="loook@mo.com", email3="inne@mol.com",
                        website="zaggfa.co.uk", address2="Selby 72",
                        homephone2="555 555 555", notes="Chief Engineer"))
    app2.logout()


def test_add__empty_contact(app2):
    app2.login(username="admin", password="secret")
    app2.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                        company="", address="", homephone="",
                        mobilephone="", workphone="", faxnumber="",
                        email1="", email2="", email3="",
                        website="", address2="",
                        homephone2="", notes=""))
    app2.logout()
