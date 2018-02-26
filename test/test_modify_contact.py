from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New Firstname"))
    new_contacts = app.contact.get_contact_list()
    # print(old_contacts)
    # print(new_contacts)
    assert (len(old_contacts)) == len(new_contacts)


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="New Lastname"))
    new_contacts = app.contact.get_contact_list()
    # print(old_contacts)
    # print(new_contacts)
    assert (len(old_contacts)) == len(new_contacts)
