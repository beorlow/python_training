from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    # print(old_contacts)
    # print(new_contacts)
    assert (len(old_contacts) - 1) == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts