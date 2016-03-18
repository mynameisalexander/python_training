# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from model.manager import Manager


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.helpers = Manager(self, SessionHelper, GroupHelper, ContactHelper)

    def open_group_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def destroy(self):
        self.wd.quit()