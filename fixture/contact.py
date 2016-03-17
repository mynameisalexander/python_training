class ContactHelper:

    def __init__(self, app):
        self.app = app
        wd = app.wd

    def general_data(self, Contact):
        wd = self.app.wd
        # open page with groups
        wd.find_element_by_link_text("add new").click()
        # filling name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        # wd.find_element_by_name("photo").click()  # selected photo
        # filling title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.title)
        # filling company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        # filling address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.address)
        # home number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home)
        # mobile number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile)
        # work number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.work)
        # fax number
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        # filling email
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contact.email3)
        # filling homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        # selected birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(Contact.bday + 2) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(Contact.bday + 2) + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(Contact.bmonth + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(Contact.bmonth + 1) + "]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.byear)
        # selected anniversary
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(Contact.aday + 2) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(Contact.aday + 2) + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(Contact.amonth + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(Contact.amonth + 1) + "]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Contact.ayear)
        # filling address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.address2)
        # phone2 number
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contact.phone2)
        # filling notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contact.notes)
        # create contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()