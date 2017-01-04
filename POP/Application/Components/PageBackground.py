from Components.Component import *
from dominate.tags import *


class PageBackground(Component):
    _description = "Sets the background of a page"
    _attributes = [('imagePath', 'string')]
    _methods = [('setBackground', 'Set imagePath to a value')]

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

    def execute(self):
        return self.printHTML()

    def __str__(self):
        return self.description()

    def __init__(self, imagePath=""):
        super().__init__()
        self.imagePath = imagePath

    def setBackground(self, imagePath=None):
        self.imagePath = imagePath

    def printHTML(self):
        image = img()
        image['src'] = self.imagePath
        image['style'] = "width: 100%; height: auto; max-width: 100%;"

        d = div(image)
        d['background-color'] = "#000000"
        return d