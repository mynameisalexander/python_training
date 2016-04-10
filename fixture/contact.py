from model.contact import Contact
import re


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
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_id(new_contact_data, 0)

    def modify_contact_by_id(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # open page by id
        wd.get('http://localhost:8080/addressbook/edit.php?id='+str(new_contact_data.id))
        self.fill_group_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def fill_group_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
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
        self.change_field_value("phone2", contact.secondphone)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if field_name is not None:
            if text == "bday":
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(field_name) + "]").is_selected()
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(field_name) + "]").click()
            elif text == "bmonth":
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(field_name) + "]").is_selected()
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(field_name) + "]").click()
            elif text == "aday":
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(field_name) + "]").is_selected()
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(field_name) + "]").click()
            elif text == "amonth":
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(field_name) + "]").is_selected()
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(field_name) + "]").click()
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
        self.contact_cache = None

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
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_email = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondphone=secondphone,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        content = wd.find_element_by_id("content")
        homephone = re.search("H: (.*)", content.text).group(1)
        mobilephone = re.search("M: (.*)", content.text).group(1)
        workphone = re.search("W: (.*)", content.text).group(1)
        secondphone = re.search("P: (.*)", content.text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondphone=secondphone)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

