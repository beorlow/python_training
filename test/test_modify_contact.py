from model.contact import Contact

def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New Firstname", middlename="Been", lastname="Modified", nickname="Onne", title="Engineer",
                        company="Engineering", address="Doscoe 6 Wisconsin", homephone="111 111 111",
                        mobilephone="222 222 222", workphone="333 333 333", faxnumber="546 789 876",
                        email1="kooll@anne.com", email2="loook@mo.com", email3="inne@mol.com",
                        website="zaggfa.co.uk", address2="Selby 72",
                        homephone2="555 555 555", notes="Chief Engineer"))
    app.session.logout()


def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Has", middlename="Been", lastname="New Lastname", nickname="Onne", title="Engineer",
                        company="Engineering", address="Doscoe 6 Wisconsin", homephone="111 111 111",
                        mobilephone="222 222 222", workphone="333 333 333", faxnumber="546 789 876",
                        email1="kooll@anne.com", email2="loook@mo.com", email3="inne@mol.com",
                        website="zaggfa.co.uk", address2="Selby 72",
                        homephone2="555 555 555", notes="Chief Engineer"))
    app.session.logout()