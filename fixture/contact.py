from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def create(self, Contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_group_form(Contact)
        # create contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def modify_first_contact(self, Contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # init contact update
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_group_form(Contact)
        # update contact
        wd.find_element_by_name("update").click()

    def fill_group_form(self, Contact):
        wd = self.app.wd
        self.change_field_value("firstname", Contact.firstname)
        self.change_field_value("middlename", Contact.middlename)
        self.change_field_value("lastname", Contact.lastname)
        self.change_field_value("nickname", Contact.nickname)
        self.change_field_value("title", Contact.title)
        self.change_field_value("company", Contact.company)
        self.change_field_value("address", Contact.address)
        self.change_field_value("home", Contact.home)
        self.change_field_value("mobile", Contact.mobile)
        self.change_field_value("work", Contact.work)
        self.change_field_value("fax", Contact.fax)
        self.change_field_value("email2", Contact.email2)
        self.change_field_value("email3", Contact.email3)
        self.change_field_value("homepage", Contact.homepage)
        self.change_field_value("bday", Contact.bday)
        self.change_field_value("bmonth", Contact.bmonth)
        self.change_field_value("byear", Contact.byear)
        self.change_field_value("aday", Contact.aday)
        self.change_field_value("amonth", Contact.amonth)
        self.change_field_value("ayear", Contact.ayear)
        self.change_field_value("address2", Contact.address2)
        self.change_field_value("phone2", Contact.phone2)
        self.change_field_value("notes", Contact.notes)

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if field_name is not None:
            if text == "bday":
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(field_name + 2) + "]").is_selected()
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(field_name + 2) + "]").click()
            elif text == "bmonth":
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(field_name + 1) + "]").is_selected()
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(field_name + 1) + "]").click()
            elif text == "aday":
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(field_name + 2) + "]").is_selected()
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(field_name + 2) + "]").click()
            elif text == "amonth":
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(field_name + 1) + "]").is_selected()
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(field_name + 1) + "]").click()
            else:
                wd.find_element_by_name(text).click()
                wd.find_element_by_name(text).clear()
                wd.find_element_by_name(text).send_keys(field_name)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            text = element.text.split()
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text[1], lastname=text[0], id=id))
        return contacts

