# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.helpers.session.login(username="admin", password="secret")
    app.helpers.group.create(Group(name="sdfgsdfg", header="sdfgdsfg", footer="sdfgsdfgs"))
    app.helpers.session.logout()


def test_add_empty_group(app):
    app.helpers.session.login(username="admin", password="secret")
    app.helpers.group.create(Group(name="", header="", footer=""))
    app.helpers.session.logout()