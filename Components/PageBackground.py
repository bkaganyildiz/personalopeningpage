from Components.Component import *


class PageBackground(Component):
    def description(self):
        return "A collection of background images which changes in a set time"

    def attributes(self):
        att = []

        for attribute in dir(self):
            if not callable(getattr(self, attribute)):
                att.append((attribute, type(getattr(self, attribute)).__name__))

        return att

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def methods(self):
        att = []

        for attribute in dir(self):
            if callable(getattr(self, attribute)):
                att.append((attribute, type(getattr(self, attribute)).__name__))

        return att

    def execute(self):
        return self.printHTML()

    def __str__(self):
        return self.description()

    def __init__(self, imagePath=None):
        super().__init__()
        if imagePath:
            self.imagePath = imagePath

    def setBackground(self, imagePath=None):
        self.imagePath = imagePath

    def printHTML(self):
        return '''<div>
        <p> page backgroudsaas </p>
</div>'''