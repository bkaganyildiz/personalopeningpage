from dominate.tags import *
import json


class Logout(object):
    _description = "Logout Page"
    _attributes = [
    ]
    _methods = [
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

    def execute(self):
        h = div(
            h1("Successfuly Logout")
        )
        return h
