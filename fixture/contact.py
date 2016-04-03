from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_group_form(contact)
        # create contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        contact_cache = None

    """
    1. раскомментировать нижеследующий кусок кода
    2. очистить список контактов и создать там 2 новых, через test_add_contact.py
    3. запустить test_modify_group.py
    """

   # def modify_first_contact(self, Contact):
   #     self.modify_contact_by_index(Contact, 0)

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # init contact update
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_group_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()
        contact_cache = None

    def fill_group_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("bday", contact.bday)
        self.change_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("aday", contact.aday)
        self.change_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.text.split()
                id = element.find_element_by_name("selected[]").get_attribute("value")
                contact_cache.append(Contact(firstname=text[1], lastname=text[0], id=id))
        return list(contact_cache)

