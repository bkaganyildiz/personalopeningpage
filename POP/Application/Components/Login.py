from dominate.tags import *
import json


class Login(object):
    _description = "Login Page"
    _attributes = [
        ('username', 'string'),
        ('password', 'string')
    ]
    _methods = [
        ('setUsername', 'Set Username'),
        ('setPassword', 'Set Password'),

        ('changeUsername', 'Change Username'),
        ('changePassword', 'Change Password'),
    ]

    def description(self):
        return self._description

    def attributes(self):
        return self._attributes

    def __getitem__(self, item):
        for attribute in self._attributes:
            if attribute[0] == item:
                return getattr(self, item)

        raise AttributeError(self.__class__.__name__ + " object has no attribute '" + item + "'")

    def __setitem__(self, key, value):
        for attribute in self._attributes:
            if attribute[0] == key:
                setattr(self, key, value)
                return

        raise AttributeError(self.__class__.__name__ + " object has no attribute '" + key + "'")

    def methods(self):
        return self._methods

    def __str__(self):
        return self.description()

    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def setUsername(self, username="") :
        self.username = username

    def changeUsername(self, username="") :
        self.username = username

    def setPassword(self, password="") :
        self.password = password

    def changePassword(self, password="") :
        self.password = password

    def execute(self):
        h = div(
            h1("Login"),
            div(label("Username", span(), "*"), input(type=self.username, autocomplete="off")),
            div(label("Set A Password", span(), "*"), input(type=self.password, autocomplete="off")),
            button("Login", type="Submit")
        )
        return h
