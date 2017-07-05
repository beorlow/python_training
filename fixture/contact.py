class ContactHelper:

    def __init__(self, app):
        self.app = app


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # go to contact page (homepage)
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        # enter modification mode
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # modify contact form
        self.fill_contact_form(new_contact_data)
        # submit contact modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_contact_page()

    def return_to_home_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def delete_first_contact(self):
        wd = self.app.wd
        #go to contact page (homepage)
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    #    def modify_first_contact(self, contact):
#        wd = self.app.wd
#        # go to contact page (homepage)
#        wd.find_element_by_link_text("home").click()
        #select first contact
#        self.select_first_contact()
        #enter modification mode
#        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #modify contact form
#        wd.find_element_by_name("firstname").click()
#        wd.find_element_by_name("firstname").clear()
#        wd.find_element_by_name("firstname").send_keys(contact.firstname)
#        wd.find_element_by_name("middlename").click()
#        wd.find_element_by_name("middlename").clear()
#        wd.find_element_by_name("middlename").send_keys(contact.middlename)
#        wd.find_element_by_name("lastname").click()
#        wd.find_element_by_name("lastname").clear()
#        wd.find_element_by_name("lastname").send_keys(contact.lastname)
#        wd.find_element_by_name("nickname").click()
#        wd.find_element_by_name("nickname").clear()
#        wd.find_element_by_name("nickname").send_keys(contact.nickname)
#        wd.find_element_by_name("title").click()
#        wd.find_element_by_name("title").clear()
#        wd.find_element_by_name("title").send_keys(contact.title)
#        wd.find_element_by_name("company").click()
#        wd.find_element_by_name("company").clear()
#        wd.find_element_by_name("company").send_keys(contact.company)
#        wd.find_element_by_name("address").click()
#        wd.find_element_by_name("address").clear()
#        wd.find_element_by_name("address").send_keys(contact.address)
#        wd.find_element_by_name("home").click()
#        wd.find_element_by_name("home").clear()
#        wd.find_element_by_name("home").send_keys(contact.homephone)
#        wd.find_element_by_name("mobile").click()
#        wd.find_element_by_name("mobile").clear()
#        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
#        wd.find_element_by_name("work").click()
#        wd.find_element_by_name("work").clear()
#        wd.find_element_by_name("work").send_keys(contact.workphone)
#        wd.find_element_by_name("fax").click()
#        wd.find_element_by_name("fax").clear()
#        wd.find_element_by_name("fax").send_keys(contact.faxnumber)
#        wd.find_element_by_name("email").click()
#        wd.find_element_by_name("email").clear()
#        wd.find_element_by_name("email").send_keys(contact.email1)
#        wd.find_element_by_name("email2").click()
#        wd.find_element_by_name("email2").clear()
#        wd.find_element_by_name("email2").send_keys(contact.email2)
#        wd.find_element_by_name("email3").click()
#        wd.find_element_by_name("email3").clear()
#        wd.find_element_by_name("email3").send_keys(contact.email3)
#        wd.find_element_by_name("homepage").click()
#        wd.find_element_by_name("homepage").clear()
#        wd.find_element_by_name("homepage").send_keys(contact.website)
#        wd.find_element_by_name("address2").click()
#        wd.find_element_by_name("address2").clear()
#        wd.find_element_by_name("address2").send_keys(contact.address2)
#        wd.find_element_by_name("phone2").click()
#        wd.find_element_by_name("phone2").clear()
#        wd.find_element_by_name("phone2").send_keys(contact.homephone2)
#        wd.find_element_by_name("notes").click()
#        wd.find_element_by_name("notes").clear()
#        wd.find_element_by_name("notes").send_keys(contact.notes)
#        #submit contact modification
#        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
#        self.return_to_home_contact_page()


    def create_contact(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_contact_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill out contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.faxnumber)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.website)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.homephone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
