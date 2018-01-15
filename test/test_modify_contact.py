from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New Firstname"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(lastname="New Lastname"))
