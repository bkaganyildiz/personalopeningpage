from dominate.tags import *
import json
import datetime


class Blog(object):
    _description = "Title and text"
    _attributes = [
        ('date', 'datetime'),
        ('title', 'string'),
        ('content', 'string')
    ]
    _methods = [
        ('setContent', 'Set Content'),
        ('setTitle', 'Set Title'),

        ('changeContent', 'Change Content'),
        ('changeTitle', 'Change Title'),
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

    def __init__(self,title="",content=""):
        self.title = title
        self.content = content
        self.date = datetime.datetime.now()

    def setTitle(self, title="") :
        self.title = title
        self.date = datetime.datetime.now()

    def changeTitle(self, title="") :
        self.title = title
        self.date = datetime.datetime.now()

    def setContent(self, content="") :
        self.content = content
        self.date = datetime.datetime.now()

    def changeContent(self, content="") :
        self.content = content
        self.date = datetime.now()

    def execute(self):
        h = div(
            h1("BLOG"),
            table(
                tr(td(self.title), td(self.date.strftime("%Y-%m-%d %H:%M:%S")),
                tr(td(p(self.content)))
            )))
        return h
